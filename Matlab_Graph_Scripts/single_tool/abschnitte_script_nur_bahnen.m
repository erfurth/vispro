werkzeug="D126"                                                         %Welches Werkzeug? D64/D126
letzteSchicht=false;                                                    %Sollen nur die letzten Schichten betrachtet werden?

tabellenname= ["ultrasonic3","ultrasonic3","ultrasonic3","ultrasonic4","ultrasonic4","ultrasonic4"];
%messwert = "vaLoadX";



messwert =["vaLoadX","vaLoadY","vaLoadZ","aaCurrX","aaCurrY","aaCurrZ"]
achsbeschreibungX = [{'Load','in %'}, {'Current','in A'}];
bahnstart = strings; bahnende = strings;
rauheitenTabelle=table;

if(werkzeug=="D64")                 %Zeiten der einzelnen Bahnen des Versuchs mit D64 Werkzeug                          
    %D64
    bahnstart(1)="20.04.2021, 14:42:19";bahnende(1)="20.04.2021, 14:45:55";
    bahnstart(end+1)="20.04.2021, 14:45:55";bahnende(end+1)="20.04.2021, 14:48:33";
    bahnstart(end+1)="20.04.2021, 14:48:34";bahnende(end+1)="20.04.2021, 14:51:11";
    bahnstart(end+1)="20.04.2021, 14:51:14";bahnende(end+1)="20.04.2021, 14:59:08";

    bahnstart(end+1)="20.04.2021, 14:59:09";bahnende(end+1)="20.04.2021, 15:01:45";
    bahnstart(end+1)="20.04.2021, 15:01:46";bahnende(end+1)="20.04.2021, 15:04:22";
    bahnstart(end+1)="20.04.2021, 15:04:22";bahnende(end+1)="20.04.2021, 15:06:59";
    bahnstart(end+1)="20.04.2021, 15:06:59";bahnende(end+1)="20.04.2021, 15:09:47";

    rauheitenTabelle.Ra= evalin('base', 'RaD64');
    rauheitenTabelle.Rq= evalin('base', 'RqD64');
    rauheitenTabelle.Rz= evalin('base', 'RzD64');
    rauheitenTabelle.Wt= evalin('base', 'WtD64');
    

else                                %Zeiten der einzelnen Bahnen des Versuchs mit D126 Werkzeug 
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
end





connectorFile = 'mysql-connector-java-8.0.21.jar';

javaaddpath(connectorFile)                          % Datenbank-Connector einbinden

conn = database("test","root","",'com.mysql.jdbc.Driver',append('jdbc:mysql://',"localhost",':',"3306",'/',"test"));

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
        beginTime=datetime(bahnstart(i),"InputFormat","dd.MM.yyyy, HH:mm:ss");      %Die Zeiten vom Format, wie es in Grafana vorliegt zum Format der Datenbank konvertieren
        beginTimeFormated=datetime(beginTime,"Format","yyyy-MM-dd HH:mm:ss");
        endTime=datetime(bahnende(i),"InputFormat","dd.MM.yyyy, HH:mm:ss");
        endTimeFormated=datetime(endTime,"Format","yyyy-MM-dd HH:mm:ss");
        if i <= 4
            xyQueryString= " AND actToolBasePosY > 70.2482 AND actToolBasePosY < 130.216 "      %Bei den Bahnen in Y-Richtung, beachte nur die Werte im Bereich um Werte vor und nach dem Materialeingriff rauszufiltern.
        else
            xyQueryString= " AND actToolBasePosX > 69.9729 AND actToolBasePosX < 129.973 "      %Selbiges bei den Bahnen in X-Richtung
        end
        timequery = append('SELECT `id` , `timestamp` FROM ',"test",'.',"ultrasonic5",' WHERE timestamp >= "',string(beginTimeFormated),'" ',' AND timestamp <= "',string(endTimeFormated),'"',' AND actToolBasePosZ <= 201.083 ',xyQueryString);   %mit actToolBasePosZ werden alle Stellen rausgefiltert, die über der Höhe der höhsten Schicht liegen.
        timedata=fetch(conn,timequery);
        id=table2array(timedata(:,1));
        timestamp=table2array(timedata(:,2));
        abschnittStart(1)=string(timestamp(1))

        for j = 2:length(id)-1
            if(id(j-1)~=id(j)-1)        %immer wenn die ID des nachfolgenden Elements nicht um 1 höher als die vorherige ID, beginnt ein neuer Abschnitt. bei jedem Abschnitt werden Anfangs- und Endzeitpunkt in eine Liste gespeichert.
                abschnittEnde(end+1)=string(timestamp(j-1));
                abschnittStart(end+1)=string(timestamp(j));
            end
        end
        abschnittEnde(1)=[];
        abschnittEnde(end+1)=string(timestamp(end));
        col=[];
        for j=1:length(abschnittStart)  %Mit den Anfangs- und Endzeitpunkten der einzelnen Abschnitte werden jetzt die eigentlichen Werte aus der Datenbank Abgerufen.
            query = append('SELECT `id` , `',messwert(m),'` , `timestamp` FROM ',"test",'.',tabellenname(m),' WHERE timestamp >= "',abschnittStart(j),'" ',' AND timestamp <= "',abschnittEnde(j),'"'); 
            assignin('base', 'query', query);
            data = fetch(conn,query);
            variablenameDurchgang=append("bahn_",num2str(i,"%02d"),"_durchgang_",num2str(j,"%02d"),"_messwert_",messwert(m));
            eval(append(variablenameDurchgang," = table2array(data(:,2));"));
            if(letzteSchicht==true)
                col=table2array(data(:,2)); %wenn nur die letzte Schicht betrachtet werden soll, wird nur das letzte Ergebnis verwendet.
            else
                col=[col;table2array(data(:,2))]; %wenn alle Schichten betrachtet werden sollen, werden alle zur liste hinzugefügt.
            end
            
        end
        
        %mit den werten werden jetzt die einzelnen Funktionen ausgeführt
        %und in variablen gespeichert.
        variablenameBahn=append("bahn_",num2str(i,"%02d"),"_komplett_messwert_",messwert(m));
        eval(append(variablenameBahn," = col;"));
        eval(append("tempMean = [tempMean;mean(",variablenameBahn,")];"))
        eval(append("means_messwert_",messwert(m)," = tempMean"))
        eval(append("tempMin = [tempMin;min(",variablenameBahn,")];"))
        eval(append("mins_messwert_",messwert(m)," = tempMin"))
        eval(append("tempMax = [tempMax;max(",variablenameBahn,")];"))
        eval(append("maxs_messwert_",messwert(m)," = tempMax"))
        eval(append("tempStd = [tempStd;std(",variablenameBahn,")];"))
        eval(append("stds_messwert_",messwert(m)," = tempStd"))
        
    end
   
end
%jetzt wird die funktion zum ploten der graphen für alle variablen
%ausgeführt.
 printPlot.printgraph(eval(append("means_messwert_",messwert(1))),eval(append("means_messwert_",messwert(2))),eval(append("means_messwert_",messwert(3))),rauheitenTabelle,werkzeug,append("means_messwert_",messwert(1)),achsbeschreibungX(1:2))
 printPlot.printgraph(eval(append("means_messwert_",messwert(4))),eval(append("means_messwert_",messwert(5))),eval(append("means_messwert_",messwert(6))),rauheitenTabelle,werkzeug,append("means_messwert_",messwert(4)),achsbeschreibungX(3:4))
 printPlot.printgraph(eval(append("mins_messwert_",messwert(1))),eval(append("mins_messwert_",messwert(2))),eval(append("mins_messwert_",messwert(3))),rauheitenTabelle,werkzeug,append("mins_messwert_",messwert(1)),achsbeschreibungX(1:2))
 printPlot.printgraph(eval(append("mins_messwert_",messwert(4))),eval(append("mins_messwert_",messwert(5))),eval(append("mins_messwert_",messwert(6))),rauheitenTabelle,werkzeug,append("mins_messwert_",messwert(4)),achsbeschreibungX(3:4))
 printPlot.printgraph(eval(append("maxs_messwert_",messwert(1))),eval(append("maxs_messwert_",messwert(2))),eval(append("maxs_messwert_",messwert(3))),rauheitenTabelle,werkzeug,append("maxs_messwert_",messwert(1)),achsbeschreibungX(1:2))
 printPlot.printgraph(eval(append("maxs_messwert_",messwert(4))),eval(append("maxs_messwert_",messwert(5))),eval(append("maxs_messwert_",messwert(6))),rauheitenTabelle,werkzeug,append("maxs_messwert_",messwert(4)),achsbeschreibungX(3:4))
 printPlot.printgraph(eval(append("stds_messwert_",messwert(1))),eval(append("stds_messwert_",messwert(2))),eval(append("stds_messwert_",messwert(3))),rauheitenTabelle,werkzeug,append("stds_messwert_",messwert(1)),achsbeschreibungX(1:2))
 printPlot.printgraph(eval(append("stds_messwert_",messwert(4))),eval(append("stds_messwert_",messwert(5))),eval(append("stds_messwert_",messwert(6))),rauheitenTabelle,werkzeug,append("stds_messwert_",messwert(4)),achsbeschreibungX(3:4))
