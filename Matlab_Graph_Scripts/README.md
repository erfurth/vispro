# Matlab Graph Scripts
Die Scripts werden dazu verwendet, Zusammenhänge zwischen den Messwerten und den Rauheiten darzustellen.

## deprecated
Die Scripts in "deprecated" sind die ersten Gehversuche. Um diese zu benutzen, müssen die Datensätze per **Matlab Database Importer** ins Workspace importiert werden. 

Das geschieht über die Zeile
```
 assignin('base', strrep(strrep(strrep(append('StdAD64_',app.dataSetName,'_',app.MesswertDropDown.Items{app.MesswertDropDown.Value}),', ','_'),'.',''),':',''),std(y));
```

## single tool
[Bild]
Mit dem "Single Tool" Script werden Graphen für ein einzelnes Werkzeug (D126 oder D64) erstellt.

## both tools
[Bild]
Das Script im "Both Tools" erstellt Graphen für beide Werkzeuge, die per Farbe zu unterscheiden sind.

## single layers
[Bild]
Im "Single Layers" Script werden Graphen erstellt, die die Werte für jede abgeschliffene Schicht einzeln darstellt.