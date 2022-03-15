classdef printPlot
   methods (Static)
        function printgraph(variableNameX,variableNameY,variableNameZ,rauheitenTabelle,werkzeug,saveName,achsenbeschriftung)
            
            valueX=variableNameX;
            valueY=variableNameY;
            valueZ=variableNameZ;
            Ra=rauheitenTabelle.Ra;
            Rq=rauheitenTabelle.Rq;
            Rz=rauheitenTabelle.Rz;
            Wt=rauheitenTabelle.Wt;
            achsbeschreibungX = achsenbeschriftung;
            achsbeschreibungY = {'Roughness','in µm'};


            label = string(1:8);
            labelOffset=0.005;

            testlayout=tiledlayout(4,3)
            nexttile
            scatter(valueX,Ra,'r');
            text(valueX,Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
        
            corr_pearson_min_vaLoad_x_Ra=corr(valueX,Ra,'Type','Pearson')
            corr_kendall_min_vaLoad_x_Ra=corr(valueX,Ra,'Type','Kendall')
            corr_spearman_min_vaLoad_x_Ra=corr(valueX,Ra,'Type','Spearman')
            title(append('x - Ra; corr = ',string(corr_pearson_min_vaLoad_x_Ra),', ',string(corr_kendall_min_vaLoad_x_Ra),', ',string(corr_spearman_min_vaLoad_x_Ra)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueY,Ra,'r');
            text(valueY,Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_y_Ra=corr(valueY,Ra,'Type','Pearson')
            corr_kendall_min_vaLoad_y_Ra=corr(valueY,Ra,'Type','Kendall')
            corr_spearman_min_vaLoad_y_Ra=corr(valueY,Ra,'Type','Spearman')
            title(append('y - Ra; corr = ',string(corr_pearson_min_vaLoad_y_Ra),', ',string(corr_kendall_min_vaLoad_y_Ra),', ',string(corr_spearman_min_vaLoad_y_Ra)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueZ,Ra,'r');

            text(valueZ,Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_z_Ra=corr(valueZ,Ra,'Type','Pearson')
            corr_kendall_min_vaLoad_z_Ra=corr(valueZ,Ra,'Type','Kendall')
            corr_spearman_min_vaLoad_z_Ra=corr(valueZ,Ra,'Type','Spearman')
            title(append('x - Ra; corr = ',string(corr_pearson_min_vaLoad_z_Ra),', ',string(corr_kendall_min_vaLoad_z_Ra),', ',string(corr_spearman_min_vaLoad_z_Ra)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueX,Rq,'r');

            text(valueX,Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_x_Rq=corr(valueX,Rq,'Type','Pearson')
            corr_kendall_min_vaLoad_x_Rq=corr(valueX,Rq,'Type','Kendall')
            corr_spearman_min_vaLoad_x_Rq=corr(valueX,Rq,'Type','Spearman')
            title(append('x - Rq; corr = ',string(corr_pearson_min_vaLoad_x_Rq),', ',string(corr_kendall_min_vaLoad_x_Rq),', ',string(corr_spearman_min_vaLoad_x_Rq)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueY,Rq,'r');

            text(valueY,Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_y_Rq=corr(valueY,Rq,'Type','Pearson')
            corr_kendall_min_vaLoad_y_Rq=corr(valueY,Rq,'Type','Kendall')
            corr_spearman_min_vaLoad_y_Rq=corr(valueY,Rq,'Type','Spearman')
            title(append('y - Rq; corr = ',string(corr_pearson_min_vaLoad_y_Rq),', ',string(corr_kendall_min_vaLoad_y_Rq),', ',string(corr_spearman_min_vaLoad_y_Rq)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueZ,Rq,'r');

            text(valueZ,Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_z_Rq=corr(valueZ,Rq,'Type','Pearson')
            corr_kendall_min_vaLoad_z_Rq=corr(valueZ,Rq,'Type','Kendall')
            corr_spearman_min_vaLoad_z_Rq=corr(valueZ,Rq,'Type','Spearman')
            title(append('z - Rq; corr = ',string(corr_pearson_min_vaLoad_z_Rq),', ',string(corr_kendall_min_vaLoad_z_Rq),', ',string(corr_spearman_min_vaLoad_z_Rq)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueX,Rz,'r');

            text(valueX,Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_x_Rz=corr(valueX,Rz,'Type','Pearson')
            corr_kendall_min_vaLoad_x_Rz=corr(valueX,Rz,'Type','Kendall')
            corr_spearman_min_vaLoad_x_Rz=corr(valueX,Rz,'Type','Spearman')
            title(append('x - Rz; corr = ',string(corr_pearson_min_vaLoad_x_Rz),', ',string(corr_kendall_min_vaLoad_x_Rz),', ',string(corr_spearman_min_vaLoad_x_Rz)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueY,Rz,'r');

            text(valueY,Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_y_Rz=corr(valueY,Rz,'Type','Pearson')
            corr_kendall_min_vaLoad_y_Rz=corr(valueY,Rz,'Type','Kendall')
            corr_spearman_min_vaLoad_y_Rz=corr(valueY,Rz,'Type','Spearman')
            title(append('y - Rz; corr = ',string(corr_pearson_min_vaLoad_y_Rz),', ',string(corr_kendall_min_vaLoad_y_Rz),', ',string(corr_spearman_min_vaLoad_y_Rz)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueZ,Rz,'r');

            text(valueZ,Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_z_Rz=corr(valueZ,Rz,'Type','Pearson')
            corr_kendall_min_vaLoad_z_Rz=corr(valueZ,Rz,'Type','Kendall')
            corr_spearman_min_vaLoad_z_Rz=corr(valueZ,Rz,'Type','Spearman')
            title(append('z - Rz; corr = ',string(corr_pearson_min_vaLoad_z_Rz),', ',string(corr_kendall_min_vaLoad_z_Rz),', ',string(corr_spearman_min_vaLoad_z_Rz)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueX,Wt,'r');

            text(valueX,Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_x_Wt=corr(valueX,Wt,'Type','Pearson')
            corr_kendall_min_vaLoad_x_Wt=corr(valueX,Wt,'Type','Kendall')
            corr_spearman_min_vaLoad_x_Wt=corr(valueX,Wt,'Type','Spearman')
            title(append('x - Wt; corr = ',string(corr_pearson_min_vaLoad_x_Wt),', ',string(corr_kendall_min_vaLoad_x_Wt),', ',string(corr_spearman_min_vaLoad_x_Wt)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueY,Wt,'r');

            text(valueY,Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_y_Wt=corr(valueY,Wt,'Type','Pearson')
            corr_kendall_min_vaLoad_y_Wt=corr(valueY,Wt,'Type','Kendall')
            corr_spearman_min_vaLoad_y_Wt=corr(valueY,Wt,'Type','Spearman')
            title(append('y - Wt; corr = ',string(corr_pearson_min_vaLoad_y_Wt),', ',string(corr_kendall_min_vaLoad_y_Wt),', ',string(corr_spearman_min_vaLoad_y_Wt)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueZ,Wt,'r');

            text(valueZ,Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_z_Wt=corr(valueZ,Wt,'Type','Pearson')
            corr_kendall_min_vaLoad_z_Wt=corr(valueZ,Wt,'Type','Kendall')
            corr_spearman_min_vaLoad_z_Wt=corr(valueZ,Wt,'Type','Spearman')
            title(append('z - Wt; corr = ',string(corr_pearson_min_vaLoad_z_Wt),', ',string(corr_kendall_min_vaLoad_z_Wt),', ',string(corr_spearman_min_vaLoad_z_Wt)))
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off
            set(gcf, 'PaperPosition', [0 0 40 30]); %x_width=10cm y_width=15cm
            saveas(testlayout,append("letzteSchicht/",werkzeug,"/",saveName,".fig"));
            saveas(testlayout,append("letzteSchicht/",werkzeug,"/",saveName,".png"));
        end
   end
end