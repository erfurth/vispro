function graph =printgraph(variableNameX,variableY,variableZ,beschriftungX="x",beschriftungY="y")
    value;
    eval(append("valueX=",variableNameX));
    eval(append("valueY=",variableNameY));
    eval(append("valueZ=",variableNameZ));
    achsbeschreibungX = {'Load min','in %'};
    achsbeschreibungY = {'Roughness','in µm'};


    label = string(1:8);
    labelOffset=0.005;

    tiledlayout(4,3)
    nexttile
    scatter(min_vaLoad.x,min_vaLoad.Ra,'r');
    text(min_vaLoad.x,min_vaLoad.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.x,minD64_vaLoad.Ra,'b')
    corr_pearson_min_vaLoad_x_Ra=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Ra,minD64_vaLoad.Ra),'Type','Pearson')
    corr_kendall_min_vaLoad_x_Ra=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Ra,minD64_vaLoad.Ra),'Type','Kendall')
    corr_spearman_min_vaLoad_x_Ra=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Ra,minD64_vaLoad.Ra),'Type','Spearman')
    title(append('x - Ra; corr = ',string(corr_pearson_min_vaLoad_x_Ra),', ',string(corr_kendall_min_vaLoad_x_Ra),', ',string(corr_spearman_min_vaLoad_x_Ra)))
    text(minD64_vaLoad.x,minD64_vaLoad.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.y,min_vaLoad.Ra,'r');
    text(min_vaLoad.y,min_vaLoad.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.y,minD64_vaLoad.Ra,'b');
    corr_pearson_min_vaLoad_y_Ra=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Ra,minD64_vaLoad.Ra),'Type','Pearson')
    corr_kendall_min_vaLoad_y_Ra=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Ra,minD64_vaLoad.Ra),'Type','Kendall')
    corr_spearman_min_vaLoad_y_Ra=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Ra,minD64_vaLoad.Ra),'Type','Spearman')
    title(append('y - Ra; corr = ',string(corr_pearson_min_vaLoad_y_Ra),', ',string(corr_kendall_min_vaLoad_y_Ra),', ',string(corr_spearman_min_vaLoad_y_Ra)))
    text(minD64_vaLoad.y,minD64_vaLoad.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.z,min_vaLoad.Ra,'r');

    text(min_vaLoad.z,min_vaLoad.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.z,minD64_vaLoad.Ra,'b');
    corr_pearson_min_vaLoad_z_Ra=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Ra,minD64_vaLoad.Ra),'Type','Pearson')
    corr_kendall_min_vaLoad_z_Ra=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Ra,minD64_vaLoad.Ra),'Type','Kendall')
    corr_spearman_min_vaLoad_z_Ra=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Ra,minD64_vaLoad.Ra),'Type','Spearman')
    title(append('x - Ra; corr = ',string(corr_pearson_min_vaLoad_z_Ra),', ',string(corr_kendall_min_vaLoad_z_Ra),', ',string(corr_spearman_min_vaLoad_z_Ra)))
    text(minD64_vaLoad.z,minD64_vaLoad.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.x,min_vaLoad.Rq,'r');

    text(min_vaLoad.x,min_vaLoad.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.x,minD64_vaLoad.Rq,'b')
    corr_pearson_min_vaLoad_x_Rq=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Rq,minD64_vaLoad.Rq),'Type','Pearson')
    corr_kendall_min_vaLoad_x_Rq=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Rq,minD64_vaLoad.Rq),'Type','Kendall')
    corr_spearman_min_vaLoad_x_Rq=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Rq,minD64_vaLoad.Rq),'Type','Spearman')
    title(append('x - Rq; corr = ',string(corr_pearson_min_vaLoad_x_Rq),', ',string(corr_kendall_min_vaLoad_x_Rq),', ',string(corr_spearman_min_vaLoad_x_Rq)))
    text(minD64_vaLoad.x,minD64_vaLoad.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.y,min_vaLoad.Rq,'r');

    text(min_vaLoad.y,min_vaLoad.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.y,minD64_vaLoad.Rq,'b');
    corr_pearson_min_vaLoad_y_Rq=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Rq,minD64_vaLoad.Rq),'Type','Pearson')
    corr_kendall_min_vaLoad_y_Rq=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Rq,minD64_vaLoad.Rq),'Type','Kendall')
    corr_spearman_min_vaLoad_y_Rq=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Rq,minD64_vaLoad.Rq),'Type','Spearman')
    title(append('y - Rq; corr = ',string(corr_pearson_min_vaLoad_y_Rq),', ',string(corr_kendall_min_vaLoad_y_Rq),', ',string(corr_spearman_min_vaLoad_y_Rq)))
    text(minD64_vaLoad.y,minD64_vaLoad.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.z,min_vaLoad.Rq,'r');

    text(min_vaLoad.z,min_vaLoad.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.z,minD64_vaLoad.Rq,'b');
    corr_pearson_min_vaLoad_z_Rq=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Rq,minD64_vaLoad.Rq),'Type','Pearson')
    corr_kendall_min_vaLoad_z_Rq=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Rq,minD64_vaLoad.Rq),'Type','Kendall')
    corr_spearman_min_vaLoad_z_Rq=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Rq,minD64_vaLoad.Rq),'Type','Spearman')
    title(append('z - Rq; corr = ',string(corr_pearson_min_vaLoad_z_Rq),', ',string(corr_kendall_min_vaLoad_z_Rq),', ',string(corr_spearman_min_vaLoad_z_Rq)))
    text(minD64_vaLoad.z,minD64_vaLoad.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.x,min_vaLoad.Rz,'r');

    text(min_vaLoad.x,min_vaLoad.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.x,minD64_vaLoad.Rz,'b')
    corr_pearson_min_vaLoad_x_Rz=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Rz,minD64_vaLoad.Rz),'Type','Pearson')
    corr_kendall_min_vaLoad_x_Rz=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Rz,minD64_vaLoad.Rz),'Type','Kendall')
    corr_spearman_min_vaLoad_x_Rz=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Rz,minD64_vaLoad.Rz),'Type','Spearman')
    title(append('x - Rz; corr = ',string(corr_pearson_min_vaLoad_x_Rz),', ',string(corr_kendall_min_vaLoad_x_Rz),', ',string(corr_spearman_min_vaLoad_x_Rz)))
    text(minD64_vaLoad.x,minD64_vaLoad.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.y,min_vaLoad.Rz,'r');

    text(min_vaLoad.y,min_vaLoad.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.y,minD64_vaLoad.Rz,'b');
    corr_pearson_min_vaLoad_y_Rz=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Rz,minD64_vaLoad.Rz),'Type','Pearson')
    corr_kendall_min_vaLoad_y_Rz=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Rz,minD64_vaLoad.Rz),'Type','Kendall')
    corr_spearman_min_vaLoad_y_Rz=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Rz,minD64_vaLoad.Rz),'Type','Spearman')
    title(append('y - Rz; corr = ',string(corr_pearson_min_vaLoad_y_Rz),', ',string(corr_kendall_min_vaLoad_y_Rz),', ',string(corr_spearman_min_vaLoad_y_Rz)))
    text(minD64_vaLoad.y,minD64_vaLoad.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.z,min_vaLoad.Rz,'r');

    text(min_vaLoad.z,min_vaLoad.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.z,minD64_vaLoad.Rz,'b');
    corr_pearson_min_vaLoad_z_Rz=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Rz,minD64_vaLoad.Rz),'Type','Pearson')
    corr_kendall_min_vaLoad_z_Rz=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Rz,minD64_vaLoad.Rz),'Type','Kendall')
    corr_spearman_min_vaLoad_z_Rz=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Rz,minD64_vaLoad.Rz),'Type','Spearman')
    title(append('z - Rz; corr = ',string(corr_pearson_min_vaLoad_z_Rz),', ',string(corr_kendall_min_vaLoad_z_Rz),', ',string(corr_spearman_min_vaLoad_z_Rz)))
    text(minD64_vaLoad.z,minD64_vaLoad.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.x,min_vaLoad.Wt,'r');

    text(min_vaLoad.x,min_vaLoad.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.x,minD64_vaLoad.Wt,'b')
    corr_pearson_min_vaLoad_x_Wt=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Wt,minD64_vaLoad.Wt),'Type','Pearson')
    corr_kendall_min_vaLoad_x_Wt=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Wt,minD64_vaLoad.Wt),'Type','Kendall')
    corr_spearman_min_vaLoad_x_Wt=corr(cat(1,min_vaLoad.x,minD64_vaLoad.x),cat(1,min_vaLoad.Wt,minD64_vaLoad.Wt),'Type','Spearman')
    title(append('x - Wt; corr = ',string(corr_pearson_min_vaLoad_x_Wt),', ',string(corr_kendall_min_vaLoad_x_Wt),', ',string(corr_spearman_min_vaLoad_x_Wt)))
    text(minD64_vaLoad.x,minD64_vaLoad.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.y,min_vaLoad.Wt,'r');

    text(min_vaLoad.y,min_vaLoad.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.y,minD64_vaLoad.Wt,'b');
    corr_pearson_min_vaLoad_y_Wt=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Wt,minD64_vaLoad.Wt),'Type','Pearson')
    corr_kendall_min_vaLoad_y_Wt=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Wt,minD64_vaLoad.Wt),'Type','Kendall')
    corr_spearman_min_vaLoad_y_Wt=corr(cat(1,min_vaLoad.y,minD64_vaLoad.y),cat(1,min_vaLoad.Wt,minD64_vaLoad.Wt),'Type','Spearman')
    title(append('y - Wt; corr = ',string(corr_pearson_min_vaLoad_y_Wt),', ',string(corr_kendall_min_vaLoad_y_Wt),', ',string(corr_spearman_min_vaLoad_y_Wt)))
    text(minD64_vaLoad.y,minD64_vaLoad.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off

    nexttile
    scatter(min_vaLoad.z,min_vaLoad.Wt,'r');

    text(min_vaLoad.z,min_vaLoad.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    hold on
    scatter(minD64_vaLoad.z,minD64_vaLoad.Wt,'b');
    corr_pearson_min_vaLoad_z_Wt=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Wt,minD64_vaLoad.Wt),'Type','Pearson')
    corr_kendall_min_vaLoad_z_Wt=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Wt,minD64_vaLoad.Wt),'Type','Kendall')
    corr_spearman_min_vaLoad_z_Wt=corr(cat(1,min_vaLoad.z,minD64_vaLoad.z),cat(1,min_vaLoad.Wt,minD64_vaLoad.Wt),'Type','Spearman')
    title(append('z - Wt; corr = ',string(corr_pearson_min_vaLoad_z_Wt),', ',string(corr_kendall_min_vaLoad_z_Wt),', ',string(corr_spearman_min_vaLoad_z_Wt)))
    text(minD64_vaLoad.z,minD64_vaLoad.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
    xlabel(achsbeschreibungX);
    ylabel(achsbeschreibungY);
    hold off
end