/**
 * The contents of this file are subject to the license and copyright
 * detailed in the LICENSE and NOTICE files at the root of the source
 * tree and available online at
 *
 * http://www.dspace.org/license/
 */
package org.dspace.storage.bitstore;

import static java.lang.String.valueOf;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.security.DigestInputStream;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.function.Supplier;

import com.amazonaws.AmazonClientException;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.AmazonS3Exception;
import com.amazonaws.services.s3.model.GetObjectRequest;
import com.amazonaws.services.s3.model.ObjectMetadata;
import com.amazonaws.services.s3.transfer.Download;
import com.amazonaws.services.s3.transfer.TransferManager;
import com.amazonaws.services.s3.transfer.TransferManagerBuilder;
import com.amazonaws.services.s3.transfer.Upload;
import jakarta.validation.constraints.NotNull;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import org.apache.commons.io.output.NullOutputStream;
import org.apache.commons.lang3.StringUtils;
import org.apache.http.HttpStatus;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.dspace.content.Bitstream;
import org.dspace.core.Utils;
import org.dspace.services.ConfigurationService;
import org.dspace.services.factory.DSpaceServicesFactory;
import org.dspace.storage.bitstore.factory.StorageServiceFactory;
import org.dspace.storage.bitstore.service.BitstreamStorageService;
import org.dspace.util.FunctionalUtils;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * Asset store using Ceph's S3-compatible Object Gateway.
 * Diese Implementierung passt den S3BitStoreService an,
 * sodass ein benutzerdefinierter Endpunkt (z. B. für Ceph) verwendet werden kann.
 * Es wird explizit ein alternativer Endpunkt gesetzt und der Zugriff im Path-Style erzwungen.
 *
 * @author Your Name
 */
public class CephS3BitStoreService extends BaseBitStoreService {
    protected static final String DEFAULT_BUCKET_PREFIX = "dspace-asset-";
    // Prefix indicating a registered bitstream
    protected final String REGISTERED_FLAG = "-R";

    private static final Logger log = LogManager.getLogger(CephS3BitStoreService.class);

    static final String CSA = "MD5";

    protected static final int digitsPerLevel = 2;
    protected static final int directoryLevels = 3;

    private boolean enabled = false;

    private String awsAccessKey;
    private String awsSecretKey;
    /**
     * Der benutzerdefinierte Endpunkt für das Ceph Object Gateway,
     * z.B. "http://meine-ceph-rgw.example.com:7480"
     */
    private String cephEndpoint;
    /**
     * AWS Region (wird hier meist nur als Platzhalter verwendet,
     * da Ceph keine Region im AWS-Sinne benötigt)
     */
    private String awsRegionName = Regions.US_EAST_1.getName();

    private boolean useRelativePath;

    /**
     * Maximale Größe eines Chunks beim Download von Ceph (Standard: 5 MB)
     */
    private long bufferSize = 5 * 1024 * 1024;

    private String bucketName = null;

    private String subfolder = null;

    private AmazonS3 s3Service = null;
    private TransferManager tm = null;

    private static final ConfigurationService configurationService
            = DSpaceServicesFactory.getInstance().getConfigurationService();

    public CephS3BitStoreService() {}

    @Override
    public boolean isEnabled() {
        return this.enabled;
    }

    /**
     * Initialisiert den Asset Store. Hier wird der AmazonS3-Client so aufgebaut,
     * dass er den benutzerdefinierten Ceph-Endpunkt nutzt und Path-Style Access erzwingt.
     */
    @Override
    public void init() throws IOException {
        if (this.isInitialized() || !this.isEnabled()) {
            return;
        }

        try {
            // Aufbau des S3-Clients mit benutzerdefiniertem Ceph-Endpunkt und Path-Style Access
            AWSCredentials credentials = null;
            if (StringUtils.isNotBlank(getAwsAccessKey()) && StringUtils.isNotBlank(getAwsSecretKey())) {
                log.info("Using configured Ceph credentials");
                credentials = new BasicAWSCredentials(getAwsAccessKey(), getAwsSecretKey());
            } else {
                log.info("No explicit credentials provided; attempting to use default credentials");
            }
            
            AmazonS3ClientBuilder builder = AmazonS3ClientBuilder.standard()
                .withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration(getCephEndpoint(), getAwsRegionName()))
                .withPathStyleAccessEnabled(true);

            if (credentials != null) {
                builder.withCredentials(new AWSStaticCredentialsProvider(credentials));
            }
            s3Service = builder.build();

            // Bucketname festlegen
            if (StringUtils.isEmpty(bucketName)) {
                String hostname = Utils.getHostName(configurationService.getProperty("dspace.ui.url"));
                bucketName = DEFAULT_BUCKET_PREFIX + hostname;
                log.warn("BucketName not configured, using default: " + bucketName);
            }

            // Bucket anlegen falls nicht vorhanden
            try {
                if (!s3Service.doesBucketExistV2(bucketName)) {
                    s3Service.createBucket(bucketName);
                    log.info("Creating new S3 Bucket: " + bucketName);
                }
            } catch (AmazonClientException e) {
                throw new IOException(e);
            }

            // Hier direkt den TransferManager bauen, anstatt FunctionalUtils.getDefaultOrBuild zu nutzen
            tm = TransferManagerBuilder.standard()
                    .withS3Client(s3Service)
                    .withAlwaysCalculateMultipartMd5(true)
                    .build();
            if (tm == null) {
                throw new IOException("TransferManager initialization failed; tm is null");
            }

            this.initialized = true;
            log.info("Ceph S3 AssetStore ready! Bucket: " + bucketName);
        } catch (Exception e) {
            this.initialized = false;
            log.error("Cannot initialize Ceph S3 AssetStore!", e);
            throw new IOException(e);
        }
    }

    @Override
    public String generateId() {
        return Utils.generateKey();
    }

    @Override
    public InputStream get(Bitstream bitstream) throws IOException {
        String key = getFullKey(bitstream.getInternalId());
        if (isRegisteredBitstream(key)) {
            key = key.substring(REGISTERED_FLAG.length());
        }
        return new S3LazyInputStream(key, bufferSize, bitstream.getSizeBytes());
    }

    @Override
    public void put(Bitstream bitstream, InputStream in) throws IOException {
        String key = getFullKey(bitstream.getInternalId());
        File scratchFile = File.createTempFile(bitstream.getInternalId(), "s3bs");
        try (FileOutputStream fos = new FileOutputStream(scratchFile);
             DigestInputStream dis = new DigestInputStream(in, MessageDigest.getInstance(CSA))) {
            Utils.bufferedCopy(dis, fos);
            in.close();

            Upload upload = tm.upload(bucketName, key, scratchFile);
            upload.waitForUploadResult();

            bitstream.setSizeBytes(scratchFile.length());
            bitstream.setChecksum(Utils.toHex(dis.getMessageDigest().digest()));
            bitstream.setChecksumAlgorithm(CSA);
        } catch (AmazonClientException | IOException | InterruptedException e) {
            log.error("put(" + bitstream.getInternalId() + ", is)", e);
            throw new IOException(e);
        } catch (NoSuchAlgorithmException nsae) {
            log.warn("Caught NoSuchAlgorithmException", nsae);
        } finally {
            if (!scratchFile.delete()) {
                scratchFile.deleteOnExit();
            }
        }
    }

    @Override
    public Map<String, Object> about(Bitstream bitstream, List<String> attrs) throws IOException {
        String key = getFullKey(bitstream.getInternalId());
        if (isRegisteredBitstream(key)) {
            key = key.substring(REGISTERED_FLAG.length());
        }

        Map<String, Object> metadata = new HashMap<>();

        try {
            ObjectMetadata objectMetadata = s3Service.getObjectMetadata(bucketName, key);
            if (objectMetadata != null) {
                putValueIfExistsKey(attrs, metadata, "size_bytes", objectMetadata.getContentLength());
                putValueIfExistsKey(attrs, metadata, "modified", valueOf(objectMetadata.getLastModified().getTime()));
            }
            putValueIfExistsKey(attrs, metadata, "checksum_algorithm", CSA);

            if (attrs.contains("checksum")) {
                try (InputStream in = get(bitstream);
                     DigestInputStream dis = new DigestInputStream(in, MessageDigest.getInstance(CSA))) {
                    Utils.copy(dis, NullOutputStream.NULL_OUTPUT_STREAM);
                    byte[] md5Digest = dis.getMessageDigest().digest();
                    metadata.put("checksum", Utils.toHex(md5Digest));
                } catch (NoSuchAlgorithmException nsae) {
                    log.warn("Caught NoSuchAlgorithmException", nsae);
                }
            }

            return metadata;
        } catch (AmazonS3Exception e) {
            if (e.getStatusCode() == HttpStatus.SC_NOT_FOUND) {
                return metadata;
            }
        } catch (AmazonClientException e) {
            log.error("about(" + key + ", attrs)", e);
            throw new IOException(e);
        }
        return metadata;
    }

    @Override
    public void remove(Bitstream bitstream) throws IOException {
        String key = getFullKey(bitstream.getInternalId());
        try {
            s3Service.deleteObject(bucketName, key);
        } catch (AmazonClientException e) {
            log.error("remove(" + key + ")", e);
            throw new IOException(e);
        }
    }

    public String getFullKey(String id) {
        StringBuilder bufFilename = new StringBuilder();
        if (StringUtils.isNotEmpty(subfolder)) {
            bufFilename.append(subfolder);
            appendSeparator(bufFilename);
        }
        if (this.useRelativePath) {
            bufFilename.append(getRelativePath(id));
        } else {
            bufFilename.append(id);
        }
        log.debug("S3 filepath for " + id + " is " + bufFilename.toString());
        return bufFilename.toString();
    }

    public String getRelativePath(String sInternalId) {
        BitstreamStorageService bitstreamStorageService = StorageServiceFactory.getInstance().getBitstreamStorageService();
        String sIntermediatePath = StringUtils.EMPTY;
        if (bitstreamStorageService.isRegisteredBitstream(sInternalId)) {
            sInternalId = sInternalId.substring(REGISTERED_FLAG.length());
        } else {
            sInternalId = sanitizeIdentifier(sInternalId);
            sIntermediatePath = getIntermediatePath(sInternalId);
        }
        return sIntermediatePath + sInternalId;
    }

    public boolean isRegisteredBitstream(String internalId) {
        return internalId.startsWith(REGISTERED_FLAG);
    }

    // Getter und Setter für die Ceph-spezifische Konfiguration
    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }

    public String getAwsAccessKey() {
        return awsAccessKey;
    }

    @Autowired(required = true)
    public void setAwsAccessKey(String awsAccessKey) {
        this.awsAccessKey = awsAccessKey;
    }

    public String getAwsSecretKey() {
        return awsSecretKey;
    }

    @Autowired(required = true)
    public void setAwsSecretKey(String awsSecretKey) {
        this.awsSecretKey = awsSecretKey;
    }

    public String getAwsRegionName() {
        return awsRegionName;
    }

    public void setAwsRegionName(String awsRegionName) {
        this.awsRegionName = awsRegionName;
    }

    public String getCephEndpoint() {
        return cephEndpoint;
    }

    public void setCephEndpoint(String cephEndpoint) {
        this.cephEndpoint = cephEndpoint;
    }

    public String getBucketName() {
        return bucketName;
    }

    @Autowired(required = true)
    public void setBucketName(String bucketName) {
        this.bucketName = bucketName;
    }

    public String getSubfolder() {
        return subfolder;
    }

    public void setSubfolder(String subfolder) {
        this.subfolder = subfolder;
    }

    public boolean isUseRelativePath() {
        return useRelativePath;
    }

    public void setUseRelativePath(boolean useRelativePath) {
        this.useRelativePath = useRelativePath;
    }

    public void setBufferSize(long bufferSize) {
        this.bufferSize = bufferSize;
    }

    // S3LazyInputStream bleibt unverändert
    public class S3LazyInputStream extends InputStream {
        private InputStream currentChunkStream;
        private String objectKey;
        private long endOfChunk = -1;
        private long chunkMaxSize;
        private long currPos = 0;
        private long fileSize;

        public S3LazyInputStream(String objectKey, long chunkMaxSize, long fileSize) throws IOException {
            this.objectKey = objectKey;
            this.chunkMaxSize = chunkMaxSize;
            this.endOfChunk = 0;
            this.fileSize = fileSize;
            downloadChunk();
        }

        @Override
        public int read() throws IOException {
            if (currPos == endOfChunk && currPos < fileSize) {
                currentChunkStream.close();
                downloadChunk();
            }
            int byteRead = currPos < endOfChunk ? currentChunkStream.read() : -1;
            if (byteRead != -1) {
                currPos++;
            } else {
                currentChunkStream.close();
            }
            return byteRead;
        }

        private void downloadChunk() throws IOException, FileNotFoundException {
            long startByte = currPos;
            long endByte = Math.min(startByte + chunkMaxSize - 1, fileSize - 1);
            GetObjectRequest getRequest = new GetObjectRequest(bucketName, objectKey).withRange(startByte, endByte);
            File currentChunkFile = File.createTempFile("s3-disk-copy-" + UUID.randomUUID(), "temp");
            currentChunkFile.deleteOnExit();
            try {
                Download download = tm.download(getRequest, currentChunkFile);
                download.waitForCompletion();
                currentChunkStream = new DeleteOnCloseFileInputStream(currentChunkFile);
                endOfChunk += download.getProgress().getBytesTransferred();
            } catch (AmazonClientException | InterruptedException e) {
                currentChunkFile.delete();
                throw new IOException(e);
            }
        }

        @Override
        public void close() throws IOException {
            if (currentChunkStream != null) {
                currentChunkStream.close();
            }
        }
    }
}
