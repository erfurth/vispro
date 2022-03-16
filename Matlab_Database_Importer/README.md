# Matlab Database Importer
[Bild]
Mit dem Matlab Database Importer lassen sich die Maschinendaten aus der Datenbank in Matlab importieren. Zusätzlich lassen sich Operationen wie z.B. die Ableitung des Graphen ausführen und zurück in die Datenbank schreiben.

## Matlab Toolbox
Um mit Matlab überhaupt Zugriff auf Datenbanken zu bekommen, muss die **Database Toolbox** installiert sein.

## MySQL Connector
Damit der Zugriff auf die Datenbank funktioniert, muss der [MySQL Connector](https://downloads.mysql.com/archives/c-j/) heruntergeladen werden. Die Datei muss entpackt und die **.jar**-Datei ins Verzeichnis der Matlab-App kopiert werden. Zusätzlich muss im Quellcode der Name des Connectors angepasst werden.
```
connectorFile = 'mysql-connector-java-8.0.21.jar';
```