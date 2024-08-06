# Matlab Continually
[Bild]
Das Matlab Continually Tool importiert ähnlich dem Database Importer die Daten von der Datenbank, jedoch kontinuierlich. Sobald neue Daten in der Datenbank sind, werden die Werte importiert, verarbeitet und die neuen Daten in eine andere Datenbanktabelle geschrieben.

## Matlab Toolbox
Um mit Matlab überhaupt Zugriff auf Datenbanken zu bekommen, muss die **Database Toolbox** installiert sein.

## MySQL Connector
Damit der Zugriff auf die Datenbank funktioniert, muss der [MySQL Connector](https://downloads.mysql.com/archives/c-j/) heruntergeladen werden. Die Datei muss entpackt und die **.jar**-Datei ins Verzeichnis der Matlab-App kopiert werden. Zusätzlich muss im Quellcode der Name des Connectors angepasst werden.
```
connectorFile = 'mysql-connector-java-8.0.21.jar';
```