import asyncio
from asyncua.crypto.cert_gen import setup_self_signed_certificate

import socket
from asyncua.crypto.truststore import TrustStore
from pathlib import Path

from cryptography.x509.oid import ExtendedKeyUsageOID


#cert_base = Path(__file__).parent
#cert = Path(cert_base / f"certificates/peer-certificate-example.der")
#private_key = Path(cert_base / f"certificates/peer-private-key-example.pem")

async def generate_cert_and_key():
    cert_base = Path(__file__).parent
    cert = Path(cert_base / f"certificates/eah_mcp_150_cert.der")
    private_key = Path(cert_base / f"certificates/eah_mcp_150_private_key.pem")

    host_name = socket.gethostname()
    client_app_uri = f"urn:freeopcua:client"

    await setup_self_signed_certificate(
        private_key,
        cert,
        client_app_uri,
        host_name,
        [ExtendedKeyUsageOID.CLIENT_AUTH],
        {
            "countryName": "DE",
            "stateOrProvinceName": "Thuringia",
            "localityName": "Jena",
            "organizationName": "EAH-Jena"
        }
    )

if __name__ == "__main__":
    asyncio.run(generate_cert_and_key())
