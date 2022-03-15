classdef printPlot_beide_versuche
   methods (Static)
        function printgraph(variableNameX,variableNameY,variableNameZ,variableNameXD64,variableNameYD64,variableNameZD64,rauheitenTabelle,werkzeug,saveName,achsenbeschriftung)
            
            valueX=variableNameX;
            valueY=variableNameY;
            valueZ=variableNameZ;
            valueXD64=variableNameXD64;
            valueYD64=variableNameYD64;
            valueZD64=variableNameZD64;
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


            label = string;
            labelOffset=0.005;

            testlayout=tiledlayout(4,3);
            title(testlayout,"\color{red}D126 \color{black}- \color{blue}D64");
            nexttile;
            scatter(valueX,Ra,'r');
            text(valueX,Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on;
        
            corr_pearson_min_vaLoad_x_Ra=corr(cat(1,valueX,valueXD64),cat(1,Ra,RaD64),'Type','Pearson');
            corr_kendall_min_vaLoad_x_Ra=corr(cat(1,valueX,valueXD64),cat(1,Ra,RaD64),'Type','Kendall');
            corr_spearman_min_vaLoad_x_Ra=corr(cat(1,valueX,valueXD64),cat(1,Ra,RaD64),'Type','Spearman');
            
            
            title(append('x - Ra; corr = ',string(corr_pearson_min_vaLoad_x_Ra),', ',string(corr_kendall_min_vaLoad_x_Ra),', ',string(corr_spearman_min_vaLoad_x_Ra)));
            scatter(valueXD64,RaD64,'b');
            text(valueXD64,RaD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile;
            scatter(valueY,Ra,'r');
            text(valueY,Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_y_Ra=corr(cat(1,valueY,valueYD64),cat(1,Ra,RaD64),'Type','Pearson');
            corr_kendall_min_vaLoad_y_Ra=corr(cat(1,valueY,valueYD64),cat(1,Ra,RaD64),'Type','Kendall');
            corr_spearman_min_vaLoad_y_Ra=corr(cat(1,valueY,valueYD64),cat(1,Ra,RaD64),'Type','Spearman');
            title(append('y - Ra; corr = ',string(corr_pearson_min_vaLoad_y_Ra),', ',string(corr_kendall_min_vaLoad_y_Ra),', ',string(corr_spearman_min_vaLoad_y_Ra)));
            scatter(valueYD64,RaD64,'b');
            text(valueYD64,RaD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off;

            nexttile;
            scatter(valueZ,Ra,'r');

            text(valueZ,Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_z_Ra=corr(cat(1,valueZ,valueZD64),cat(1,Ra,RaD64),'Type','Pearson');
            corr_kendall_min_vaLoad_z_Ra=corr(cat(1,valueZ,valueZD64),cat(1,Ra,RaD64),'Type','Kendall');
            corr_spearman_min_vaLoad_z_Ra=corr(cat(1,valueZ,valueZD64),cat(1,Ra,RaD64),'Type','Spearman');
            title(append('z - Ra; corr = ',string(corr_pearson_min_vaLoad_z_Ra),', ',string(corr_kendall_min_vaLoad_z_Ra),', ',string(corr_spearman_min_vaLoad_z_Ra)));
            scatter(valueZD64,RaD64,'b');
            text(valueZD64,RaD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off

            nexttile
            scatter(valueX,Rq,'r');

            text(valueX,Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_x_Rq=corr(cat(1,valueX,valueXD64),cat(1,Rq,RqD64),'Type','Pearson');
            corr_kendall_min_vaLoad_x_Rq=corr(cat(1,valueX,valueXD64),cat(1,Rq,RqD64),'Type','Kendall');
            corr_spearman_min_vaLoad_x_Rq=corr(cat(1,valueX,valueXD64),cat(1,Rq,RqD64),'Type','Spearman');
            title(append('x - Rq; corr = ',string(corr_pearson_min_vaLoad_x_Rq),', ',string(corr_kendall_min_vaLoad_x_Rq),', ',string(corr_spearman_min_vaLoad_x_Rq)));
            scatter(valueXD64,RqD64,'b');
            text(valueXD64,RqD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off;

            nexttile;
            scatter(valueY,Rq,'r');

            text(valueY,Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_y_Rq=corr(cat(1,valueY,valueYD64),cat(1,Rq,RqD64),'Type','Pearson');
            corr_kendall_min_vaLoad_y_Rq=corr(cat(1,valueY,valueYD64),cat(1,Rq,RqD64),'Type','Kendall');
            corr_spearman_min_vaLoad_y_Rq=corr(cat(1,valueY,valueYD64),cat(1,Rq,RqD64),'Type','Spearman');
            title(append('y - Rq; corr = ',string(corr_pearson_min_vaLoad_y_Rq),', ',string(corr_kendall_min_vaLoad_y_Rq),', ',string(corr_spearman_min_vaLoad_y_Rq)));
            scatter(valueYD64,RqD64,'b');
            text(valueYD64,RqD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off;

            nexttile;
            scatter(valueZ,Rq,'r');

            text(valueZ,Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_z_Rq=corr(cat(1,valueZ,valueZD64),cat(1,Rq,RqD64),'Type','Pearson');
            corr_kendall_min_vaLoad_z_Rq=corr(cat(1,valueZ,valueZD64),cat(1,Rq,RqD64),'Type','Kendall');
            corr_spearman_min_vaLoad_z_Rq=corr(cat(1,valueZ,valueZD64),cat(1,Rq,RqD64),'Type','Spearman');
            title(append('z - Rq; corr = ',string(corr_pearson_min_vaLoad_z_Rq),', ',string(corr_kendall_min_vaLoad_z_Rq),', ',string(corr_spearman_min_vaLoad_z_Rq)));
            scatter(valueZD64,RqD64,'b');
            text(valueZD64,RqD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off;

            nexttile;
            scatter(valueX,Rz,'r');

            text(valueX,Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_x_Rz=corr(cat(1,valueX,valueXD64),cat(1,Rz,RzD64),'Type','Pearson');
            corr_kendall_min_vaLoad_x_Rz=corr(cat(1,valueX,valueXD64),cat(1,Rz,RzD64),'Type','Kendall');
            corr_spearman_min_vaLoad_x_Rz=corr(cat(1,valueX,valueXD64),cat(1,Rz,RzD64),'Type','Spearman');
            title(append('x - Rz; corr = ',string(corr_pearson_min_vaLoad_x_Rz),', ',string(corr_kendall_min_vaLoad_x_Rz),', ',string(corr_spearman_min_vaLoad_x_Rz)));
            scatter(valueXD64,RzD64,'b');
            text(valueXD64,RzD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off;

            nexttile;
            scatter(valueY,Rz,'r');

            text(valueY,Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on;
            corr_pearson_min_vaLoad_y_Rz=corr(cat(1,valueY,valueYD64),cat(1,Rz,RzD64),'Type','Pearson');
            corr_kendall_min_vaLoad_y_Rz=corr(cat(1,valueY,valueYD64),cat(1,Rz,RzD64),'Type','Kendall');
            corr_spearman_min_vaLoad_y_Rz=corr(cat(1,valueY,valueYD64),cat(1,Rz,RzD64),'Type','Spearman');
            title(append('y - Rz; corr = ',string(corr_pearson_min_vaLoad_y_Rz),', ',string(corr_kendall_min_vaLoad_y_Rz),', ',string(corr_spearman_min_vaLoad_y_Rz)));
            scatter(valueYD64,RzD64,'b');
            text(valueYD64,RzD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off;

            nexttile;
            scatter(valueZ,Rz,'r');

            text(valueZ,Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on;
            corr_pearson_min_vaLoad_z_Rz=corr(cat(1,valueZ,valueZD64),cat(1,Rz,RzD64),'Type','Pearson');
            corr_kendall_min_vaLoad_z_Rz=corr(cat(1,valueZ,valueZD64),cat(1,Rz,RzD64),'Type','Kendall');
            corr_spearman_min_vaLoad_z_Rz=corr(cat(1,valueZ,valueZD64),cat(1,Rz,RzD64),'Type','Spearman');
            title(append('z - Rz; corr = ',string(corr_pearson_min_vaLoad_z_Rz),', ',string(corr_kendall_min_vaLoad_z_Rz),', ',string(corr_spearman_min_vaLoad_z_Rz)));
            scatter(valueZD64,RzD64,'b');
            text(valueZD64,RzD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off;

            nexttile;
            scatter(valueX,Wt,'r');

            text(valueX,Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_x_Wt=corr(cat(1,valueX,valueXD64),cat(1,Wt,WtD64),'Type','Pearson');
            corr_kendall_min_vaLoad_x_Wt=corr(cat(1,valueX,valueXD64),cat(1,Wt,WtD64),'Type','Kendall');
            corr_spearman_min_vaLoad_x_Wt=corr(cat(1,valueX,valueXD64),cat(1,Wt,WtD64),'Type','Spearman');
            title(append('x - Wt; corr = ',string(corr_pearson_min_vaLoad_x_Wt),', ',string(corr_kendall_min_vaLoad_x_Wt),', ',string(corr_spearman_min_vaLoad_x_Wt)));
            scatter(valueXD64,WtD64,'b');
            text(valueXD64,WtD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off;

            nexttile;
            scatter(valueY,Wt,'r');

            text(valueY,Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_y_Wt=corr(cat(1,valueY,valueYD64),cat(1,Wt,WtD64),'Type','Pearson');
            corr_kendall_min_vaLoad_y_Wt=corr(cat(1,valueY,valueYD64),cat(1,Wt,WtD64),'Type','Kendall');
            corr_spearman_min_vaLoad_y_Wt=corr(cat(1,valueY,valueYD64),cat(1,Wt,WtD64),'Type','Spearman');
            title(append('y - Wt; corr = ',string(corr_pearson_min_vaLoad_y_Wt),', ',string(corr_kendall_min_vaLoad_y_Wt),', ',string(corr_spearman_min_vaLoad_y_Wt)));
            scatter(valueYD64,WtD64,'b');
            text(valueYD64,WtD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off;

            nexttile;
            scatter(valueZ,Wt,'r');

            text(valueZ,Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            hold on
            corr_pearson_min_vaLoad_z_Wt=corr(cat(1,valueZ,valueZD64),cat(1,Wt,WtD64),'Type','Pearson');
            corr_kendall_min_vaLoad_z_Wt=corr(cat(1,valueZ,valueZD64),cat(1,Wt,WtD64),'Type','Kendall');
            corr_spearman_min_vaLoad_z_Wt=corr(cat(1,valueZ,valueZD64),cat(1,Wt,WtD64),'Type','Spearman');
            title(append('z - Wt; corr = ',string(corr_pearson_min_vaLoad_z_Wt),', ',string(corr_kendall_min_vaLoad_z_Wt),', ',string(corr_spearman_min_vaLoad_z_Wt)));
            scatter(valueZD64,WtD64,'b');
            text(valueZD64,WtD64+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
            xlabel(achsbeschreibungX);
            ylabel(achsbeschreibungY);
            hold off;
            set(gcf, 'PaperPosition', [0 0 40 30]); %x_width=10cm y_width=15cm
            saveas(testlayout,append("letzteSchicht/",werkzeug,"/",saveName,".fig"));
            saveas(testlayout,append("letzteSchicht/",werkzeug,"/",saveName,".png"));
%             saveas(testlayout,append("letzteSchicht/nurX/",werkzeug,"/",saveName,".fig"));
%             saveas(testlayout,append("letzteSchicht/nurX/",werkzeug,"/",saveName,".png"));
%             saveas(testlayout,append("alleSchichten/nurY/",werkzeug,"/",saveName,".fig"));
%             saveas(testlayout,append("alleSchichten/nurY/",werkzeug,"/",saveName,".png"));
%             saveas(testlayout,append("test/",werkzeug,"/",saveName,".fig"));
%             saveas(testlayout,append("test/",werkzeug,"/",saveName,".png"));
           
        end
   end
end