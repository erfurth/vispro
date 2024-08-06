werkzeug="Beide"
letzteSchicht=false;

tabellenname= ["ultrasonic3","ultrasonic3","ultrasonic3","ultrasonic4","ultrasonic4","ultrasonic4"];
%messwert = "vaLoadX";



messwert =["vaLoadX","vaLoadY","vaLoadZ","aaCurrX","aaCurrY","aaCurrZ"]
achsbeschreibungX = [{'Load','in %'}, {'Current','in A'}];
bahnstartD64 = strings; bahnendeD64 = strings;
bahnstart = strings; bahnende = strings;
rauheitenTabelle=table;
AlleWerte=table();

connectorFile = 'mysql-connector-java-8.0.21.jar';

javaaddpath(connectorFile)                          % Datenbank-Connector einbinden

conn = database("test","root","",'com.mysql.jdbc.Driver',append('jdbc:mysql://',"localhost",':',"3306",'/',"test"));


tool="D64";
    %D64
    bahnstartD64(1)="20.04.2021, 14:42:19";bahnendeD64(1)="20.04.2021, 14:45:55";
    bahnstartD64(end+1)="20.04.2021, 14:45:55";bahnendeD64(end+1)="20.04.2021, 14:48:33";
    bahnstartD64(end+1)="20.04.2021, 14:48:34";bahnendeD64(end+1)="20.04.2021, 14:51:11";
    bahnstartD64(end+1)="20.04.2021, 14:51:14";bahnendeD64(end+1)="20.04.2021, 14:59:08";

    bahnstartD64(end+1)="20.04.2021, 14:59:09";bahnendeD64(end+1)="20.04.2021, 15:01:45";
    bahnstartD64(end+1)="20.04.2021, 15:01:46";bahnendeD64(end+1)="20.04.2021, 15:04:22";
    bahnstartD64(end+1)="20.04.2021, 15:04:22";bahnendeD64(end+1)="20.04.2021, 15:06:59";
    bahnstartD64(end+1)="20.04.2021, 15:06:59";bahnendeD64(end+1)="20.04.2021, 15:09:47";

    rauheitenTabelle.RaD64= evalin('base', 'RaD64');
    rauheitenTabelle.RqD64= evalin('base', 'RqD64');
    rauheitenTabelle.RzD64= evalin('base', 'RzD64');
    rauheitenTabelle.WtD64= evalin('base', 'WtD64');
    
    for m=1:length(messwert)
    tempMeanD64=[];
    tempMinD64=[];
    tempMaxD64=[];
    tempStdD64=[];
    for i = 1:length(bahnstartD64)
        abschnittStartD64=strings;
        abschnittEndeD64=strings;
        beginTimeD64=datetime(bahnstartD64(i),"InputFormat","dd.MM.yyyy, HH:mm:ss");
        beginTimeFormatedD64=datetime(beginTimeD64,"Format","yyyy-MM-dd HH:mm:ss");
        endTimeD64=datetime(bahnendeD64(i),"InputFormat","dd.MM.yyyy, HH:mm:ss");
        endTimeFormatedD64=datetime(endTimeD64,"Format","yyyy-MM-dd HH:mm:ss");
        if i <= 4
            xyQueryString= " AND actToolBasePosY > 70.2482 AND actToolBasePosY < 130.216 ";
        else
            xyQueryString= " AND actToolBasePosX > 69.9729 AND actToolBasePosX < 129.973 ";
        end
        timequeryD64 = append('SELECT `id` , `timestamp` FROM ',"test",'.',"ultrasonic5",' WHERE timestamp >= "',string(beginTimeFormatedD64),'" ',' AND timestamp <= "',string(endTimeFormatedD64),'"',' AND actToolBasePosZ <= 201.083 ',xyQueryString); 
        timedataD64=fetch(conn,timequeryD64);
        idD64=table2array(timedataD64(:,1));
        timestampD64=table2array(timedataD64(:,2));
        abschnittStartD64(1)=string(timestampD64(1));

        for j = 2:length(idD64)-1
            if(idD64(j-1)~=idD64(j)-1)
                %disp(append(string(id(j-1)+1),":",string(timestamp(j-1)),"       ",string(id(j)),":",string(timestamp(j))))
                abschnittEndeD64(end+1)=string(timestampD64(j-1));
                abschnittStartD64(end+1)=string(timestampD64(j));
            end
        end
        abschnittEndeD64(1)=[];
        abschnittEndeD64(end+1)=string(timestampD64(end));
        col=[];
        for j=1:length(abschnittStartD64)
            query = append('SELECT `id` , `',messwert(m),'` , `timestamp` FROM ',"test",'.',tabellenname(m),' WHERE timestamp >= "',abschnittStartD64(j),'" ',' AND timestamp <= "',abschnittEndeD64(j),'"'); 
            assignin('base', 'query', query);
            dataD64 = fetch(conn,query);
            variablenameDurchgangD64=append("bahnD64_",num2str(i,"%02d"),"_durchgang_",num2str(j,"%02d"),"_messwert_",messwert(m));
            eval(append(variablenameDurchgangD64," = table2array(dataD64(:,2));"));
            if(letzteSchicht==true)
                col=table2array(dataD64(:,2));
            else
                col=[col;table2array(dataD64(:,2))];
            end
            
        end
        variablenameBahnD64=append("bahn_",num2str(i,"%02d"),"_komplett_messwert_",messwert(m));
        eval(append(variablenameBahnD64," = col;"));
        eval(append("tempMeanD64 = [tempMeanD64;mean(",variablenameBahnD64,")];"));
        eval(append("meansD64_messwert_",messwert(m)," = tempMeanD64"));
        eval(append("tempMinD64 = [tempMinD64;min(",variablenameBahnD64,")];"));
        eval(append("minsD64_messwert_",messwert(m)," = tempMinD64"));
        eval(append("tempMaxD64 = [tempMaxD64;max(",variablenameBahnD64,")];"));
        eval(append("maxsD64_messwert_",messwert(m)," = tempMaxD64"));
        eval(append("tempStdD64 = [tempStdD64;std(",variablenameBahnD64,")];"));
        eval(append("stdsD64_messwert_",messwert(m)," = tempStdD64"));
        
    end
   
end
    

    %D126
    bahnstart(1)="14.04.2021, 17:34:21";bahnende(1)="14.04.2021, 17:42:11";
    bahnstart(end+1)="14.04.2021, 17:42:12";bahnende(end+1)="14.04.2021, 17:46:53";
    bahnstart(end+1)="14.04.2021, 17:46:53";bahnende(end+1)="14.04.2021, 17:51:34";
    bahnstart(end+1)="14.04.2021, 17:51:35";bahnende(end+1)="14.04.2021, 17:56:15";

    bahnstart(end+1)="14.04.2021, 17:56:16";bahnende(end+1)="14.04.2021, 18:00:56";
    bahnstart(end+1)="14.04.2021, 18:00:57";bahnende(end+1)="14.04.2021, 18:05:36";
    bahnstart(end+1)="14.04.2021, 18:05:37";bahnende(end+1)="14.04.2021, 18:10:17";
    bahnstart(end+1)="14.04.2021, 18:10:18";bahnende(end+1)="14.04.2021, 18:15:52";

    rauheitenTabelle.Ra= evalin('base', 'Ra');
    rauheitenTabelle.Rq= evalin('base', 'Rq');
    rauheitenTabelle.Rz= evalin('base', 'Rz');
    rauheitenTabelle.Wt= evalin('base', 'Wt');









%maximale höhe: 201.083
%maxY=150,216 minY=50,2482
%maxX=149,973 minX=49,9729
for m=1:length(messwert)
    tempMean=[];
    tempMin=[];
    tempMax=[];
    tempStd=[];
    for i = 1:length(bahnstart)
        abschnittStart=strings;
        abschnittEnde=strings;
        beginTime=datetime(bahnstart(i),"InputFormat","dd.MM.yyyy, HH:mm:ss");
        beginTimeFormated=datetime(beginTime,"Format","yyyy-MM-dd HH:mm:ss");
        endTime=datetime(bahnende(i),"InputFormat","dd.MM.yyyy, HH:mm:ss");
        endTimeFormated=datetime(endTime,"Format","yyyy-MM-dd HH:mm:ss");
        if i <= 4
            xyQueryString= " AND actToolBasePosY > 70.2482 AND actToolBasePosY < 130.216 ";
        else
            xyQueryString= " AND actToolBasePosX > 69.9729 AND actToolBasePosX < 129.973 ";
        end
        timequery = append('SELECT `id` , `timestamp` FROM ',"test",'.',"ultrasonic5",' WHERE timestamp >= "',string(beginTimeFormated),'" ',' AND timestamp <= "',string(endTimeFormated),'"',' AND actToolBasePosZ <= 194.952 ',xyQueryString); 
        timedata=fetch(conn,timequery);
        id=table2array(timedata(:,1));
        timestamp=table2array(timedata(:,2));
        abschnittStart(1)=string(timestamp(1));

        for j = 2:length(id)-1
            if(id(j-1)~=id(j)-1)
                %disp(append(string(id(j-1)+1),":",string(timestamp(j-1)),"       ",string(id(j)),":",string(timestamp(j))))
                abschnittEnde(end+1)=string(timestamp(j-1));
                abschnittStart(end+1)=string(timestamp(j));
            end
        end
        abschnittEnde(1)=[];
        abschnittEnde(end+1)=string(timestamp(end));
        col=[];
        for j=1:length(abschnittStart)
            query = append('SELECT `id` , `',messwert(m),'` , `timestamp` FROM ',"test",'.',tabellenname(m),' WHERE timestamp >= "',abschnittStart(j),'" ',' AND timestamp <= "',abschnittEnde(j),'"'); 
            assignin('base', 'query', query);
            data = fetch(conn,query);
            variablenameDurchgang=append("bahn_",num2str(i,"%02d"),"_durchgang_",num2str(j,"%02d"),"_messwert_",messwert(m));
            eval(append(variablenameDurchgang," = table2array(data(:,2));"));
            if(letzteSchicht==true)
                col=table2array(data(:,2));
            else
                col=[col;table2array(data(:,2))];
            end
            
        end
        variablenameBahn=append("bahn_",num2str(i,"%02d"),"_komplett_messwert_",messwert(m));
        eval(append(variablenameBahn," = col;"));
        eval(append("tempMean = [tempMean;mean(",variablenameBahn,")];"));
        eval(append("means_messwert_",messwert(m)," = tempMean"));
        eval(append("tempMin = [tempMin;min(",variablenameBahn,")];"));
        eval(append("mins_messwert_",messwert(m)," = tempMin"));
        eval(append("tempMax = [tempMax;max(",variablenameBahn,")];"));
        eval(append("maxs_messwert_",messwert(m)," = tempMax"));
        eval(append("tempStd = [tempStd;std(",variablenameBahn,")];"));
        eval(append("stds_messwert_",messwert(m)," = tempStd"));
        
    end
   
end
 printPlot_beide_versuche.printgraph(eval(append("means_messwert_",messwert(1))),eval(append("means_messwert_",messwert(2))),eval(append("means_messwert_",messwert(3))),eval(append("meansD64_messwert_",messwert(1))),eval(append("meansD64_messwert_",messwert(2))),eval(append("meansD64_messwert_",messwert(3))),rauheitenTabelle,werkzeug,append("means_messwert_",messwert(1)),achsbeschreibungX(1:2));
 printPlot_beide_versuche.printgraph(eval(append("means_messwert_",messwert(4))),eval(append("means_messwert_",messwert(5))),eval(append("means_messwert_",messwert(6))),eval(append("meansD64_messwert_",messwert(4))),eval(append("meansD64_messwert_",messwert(5))),eval(append("meansD64_messwert_",messwert(6))),rauheitenTabelle,werkzeug,append("means_messwert_",messwert(4)),achsbeschreibungX(3:4));
 printPlot_beide_versuche.printgraph(eval(append("mins_messwert_",messwert(1))),eval(append("mins_messwert_",messwert(2))),eval(append("mins_messwert_",messwert(3))),eval(append("minsD64_messwert_",messwert(1))),eval(append("minsD64_messwert_",messwert(2))),eval(append("minsD64_messwert_",messwert(3))),rauheitenTabelle,werkzeug,append("mins_messwert_",messwert(1)),achsbeschreibungX(1:2));
 printPlot_beide_versuche.printgraph(eval(append("mins_messwert_",messwert(4))),eval(append("mins_messwert_",messwert(5))),eval(append("mins_messwert_",messwert(6))),eval(append("minsD64_messwert_",messwert(4))),eval(append("minsD64_messwert_",messwert(5))),eval(append("minsD64_messwert_",messwert(6))),rauheitenTabelle,werkzeug,append("mins_messwert_",messwert(4)),achsbeschreibungX(3:4));
 printPlot_beide_versuche.printgraph(eval(append("maxs_messwert_",messwert(1))),eval(append("maxs_messwert_",messwert(2))),eval(append("maxs_messwert_",messwert(3))),eval(append("maxsD64_messwert_",messwert(1))),eval(append("maxsD64_messwert_",messwert(2))),eval(append("maxsD64_messwert_",messwert(3))),rauheitenTabelle,werkzeug,append("maxs_messwert_",messwert(1)),achsbeschreibungX(1:2));
 printPlot_beide_versuche.printgraph(eval(append("maxs_messwert_",messwert(4))),eval(append("maxs_messwert_",messwert(5))),eval(append("maxs_messwert_",messwert(6))),eval(append("maxsD64_messwert_",messwert(4))),eval(append("maxsD64_messwert_",messwert(5))),eval(append("maxsD64_messwert_",messwert(6))),rauheitenTabelle,werkzeug,append("maxs_messwert_",messwert(4)),achsbeschreibungX(3:4));
 printPlot_beide_versuche.printgraph(eval(append("stds_messwert_",messwert(1))),eval(append("stds_messwert_",messwert(2))),eval(append("stds_messwert_",messwert(3))),eval(append("stdsD64_messwert_",messwert(1))),eval(append("stdsD64_messwert_",messwert(2))),eval(append("stdsD64_messwert_",messwert(3))),rauheitenTabelle,werkzeug,append("stds_messwert_",messwert(1)),achsbeschreibungX(1:2));
 printPlot_beide_versuche.printgraph(eval(append("stds_messwert_",messwert(4))),eval(append("stds_messwert_",messwert(5))),eval(append("stds_messwert_",messwert(6))),eval(append("stdsD64_messwert_",messwert(4))),eval(append("stdsD64_messwert_",messwert(5))),eval(append("stdsD64_messwert_",messwert(6))),rauheitenTabelle,werkzeug,append("stds_messwert_",messwert(4)),achsbeschreibungX(3:4));
