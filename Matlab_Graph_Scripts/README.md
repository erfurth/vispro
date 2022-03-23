# Matlab Graph Scripts
Die Scripts werden dazu verwendet, Zusammenhänge zwischen den Messwerten und den Rauheiten darzustellen.

## deprecated
Die Scripts in "deprecated" sind die ersten Gehversuche. Um diese zu benutzen, müssen die Datensätze per **Matlab Database Importer** ins Workspace importiert werden. 

Das geschieht über die Zeile
```
 assignin('base', strrep(strrep(strrep(append('StdAD64_',app.dataSetName,'_',app.MesswertDropDown.Items{app.MesswertDropDown.Value}),', ','_'),'.',''),':',''),std(y));
```

## single tool
![Bild](/../Pictures/single_tool.png)
Mit dem "Single Tool" Script werden Graphen für ein einzelnes Werkzeug (D126 oder D64) erstellt.

## both tools
![Bild](/../Pictures/both_tools.png)
Das Script im "Both Tools" erstellt Graphen für beide Werkzeuge, die per Farbe zu unterscheiden sind.

## single layers
![Bild](/../Pictures/single_layers.png)
Im "Single Layers" Script werden Graphen erstellt, die die Werte für jede abgeschliffene Schicht einzeln darstellt.

## multi dimension plot
![Bild](/../Pictures/multi_dimension_plot.png)
Im "Multi Dimension Plot" werden viele Messwerte auf einen 2D-Plot dargestellt

## prediction
![Bild](/../Pictures/predict.png)
Das Prediction Script sind die ersten Gehversuche mit der KI von Matlab. Bei dem Versuch wurden 2/3 eines Datensatzes zum Trainieren verwendet und anschließend wird die Vorhersage mit dem letzten Drittel verglichen.

