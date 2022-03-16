# deprecated
Die Scripts in "deprecated" sind die ersten Gehversuche. Um diese zu benutzen, müssen die Datensätze per **Matlab Database Importer** ins Workspace importiert werden. Das geschieht über die Zeile
```
 assignin('base', strrep(strrep(strrep(append('StdAD64_',app.dataSetName,'_',app.MesswertDropDown.Items{app.MesswertDropDown.Value}),', ','_'),'.',''),':',''),std(y));
```
Der String ("StdAD64_") und die Funktion (std(y)) muss dementsprechend händisch auf den gewünschten Wert (min, max, mean) angepasst werden.
Nach der Anpassung müssen alle Bahnen einmal geladen werden, damit sie ins Matlab Workspace geladen werden.

Das Script **BuildTables** erstellt dann eine Datenstruktur, die zur Weiterverarbeitung verwendet wird.
Mit dem passenden "zusammenhaenge"-Script lassen sich danach die Plots erstellen.