classdef printPlot_schichten_einzeln
   methods (Static)
        function printgraph(AlleWerte,rauheitenTabelle,saveName,achsenbeschriftung)
            
            labelOffset=0.005;

            
            messwerte=["aaCurr","vaLoad"]
            achse=["X","Y","Z"]
            werkzeuge=["D64","D126"]
            funktion =["min","max","mean","std"]
            
            test= AlleWerte(AlleWerte.Messwert=="aaCurrX"&AlleWerte.Funktion=="mean",:);
            

            Ra=rauheitenTabelle.Ra;
            Rq=rauheitenTabelle.Rq;
            Rz=rauheitenTabelle.Rz;
            Wt=rauheitenTabelle.Wt;
            RaD64=rauheitenTabelle.RaD64;
            RqD64=rauheitenTabelle.RqD64;
            RzD64=rauheitenTabelle.RzD64;
            WtD64=rauheitenTabelle.WtD64;
            achsbeschreibungX = achsenbeschriftung;
            achsbeschreibungY = {'Roughness','in µm'};
            
            
            for f=1:length(funktion)        %Schleife für die Funktion (min, max, mean, std)
                for m=1:length(messwerte)
                    markerColor = jet(14)
                    figure;
                    testlayout=tiledlayout(3,4);
                    title(testlayout,funktion(f))
                    
                    
                   
                    
                    for a=1:length(achse)       %Schleife für die Achsen (X, Y, Z)
                        query= AlleWerte(AlleWerte.Messwert==append(messwerte(m),achse(a))&AlleWerte.Funktion==funktion(f),:);      %Nehme alle werte mit der aktuellen Funktion, Achse und Messwert aus der AlleWerte Tabelle
                        
                        nexttile;
                        title(append(messwerte(m),achse(a)," - Ra"));
                        D64Query=query(query.Werkzeug==werkzeuge(2),:); %filter nach Werkzeug

                        hold on;
                        for i = 1:height(D64Query)  %Schleife für die verschiedenen Farben
                            scatter(D64Query.Wert(i),Ra(D64Query.Bahn(i)), 'MarkerEdgeColor', markerColor(D64Query.Schicht(i),:));
                        end
                        
                        hold off;
                        
                        
                        nexttile;
                        title(append(messwerte(m),achse(a)," - Rq"))
                        D64Query=query(query.Werkzeug==werkzeuge(2),:);

                        hold on;
                        for i = 1:height(D64Query)
                            scatter(D64Query.Wert(i),Rq(D64Query.Bahn(i)), 'MarkerEdgeColor', markerColor(D64Query.Schicht(i),:));
                        end
                        
                        hold off;
                        
                        
                        nexttile;
                        title(append(messwerte(m),achse(a)," - Rz"))
                        D64Query=query(query.Werkzeug==werkzeuge(2),:);

                        hold on;
                        for i = 1:height(D64Query)
                            scatter(D64Query.Wert(i),Rz(D64Query.Bahn(i)), 'MarkerEdgeColor', markerColor(D64Query.Schicht(i),:));
                        end
                        
                        hold off;
                        
                        
                        nexttile;
                        title(append(messwerte(m),achse(a)," - Wt"))
                        D64Query=query(query.Werkzeug==werkzeuge(2),:);

                        hold on;
                        for i = 1:height(D64Query)
                            scatter(D64Query.Wert(i),Wt(D64Query.Bahn(i)), 'MarkerEdgeColor', markerColor(D64Query.Schicht(i),:));
                        end
                        
                        hold off;

                    end
                    %colorbar für die einzelnen
                    cb = colorbar;
                    caxis([1 14]) 
                    colormap(jet)
                    cb.Layout.Tile = 'east';
                    %Speichern der Plots als png und als fig
                    saveas(testlayout,append("schichten_einzeln/",funktion(f),"_",messwerte(m),"_D126.fig"));
                    saveas(testlayout,append("schichten_einzeln/",funktion(f),"_",messwerte(m),"_D126.png"));
                end
            
            end          
            

%            
        end
   end
end