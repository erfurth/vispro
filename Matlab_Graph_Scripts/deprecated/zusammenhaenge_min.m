title('D126');
label = string(1:8);
labelOffset=0.005;

tiledlayout(4,3)
nexttile
scatter(min_CurrTable.x,min_CurrTable.Ra,'r');
title('y - Ra')
text(min_CurrTable.x,min_CurrTable.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.x,min_CurrTableD64.Ra,'b')
title('x - Ra')
text(min_CurrTableD64.x,min_CurrTableD64.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.y,min_CurrTable.Ra,'r');
title('y - Ra')
text(min_CurrTable.y,min_CurrTable.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.y,min_CurrTableD64.Ra,'b');
title('y - Ra')
text(min_CurrTableD64.y,min_CurrTableD64.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.z,min_CurrTable.Ra,'r');
title('z - Ra')
text(min_CurrTable.z,min_CurrTable.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.z,min_CurrTableD64.Ra,'b');
title('z - Ra')
text(min_CurrTableD64.z,min_CurrTableD64.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.x,min_CurrTable.Rq,'r');
title('y - Rq')
text(min_CurrTable.x,min_CurrTable.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.x,min_CurrTableD64.Rq,'b')
title('x - Rq')
text(min_CurrTableD64.x,min_CurrTableD64.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.y,min_CurrTable.Rq,'r');
title('y - Rq')
text(min_CurrTable.y,min_CurrTable.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.y,min_CurrTableD64.Rq,'b');
title('y - Rq')
text(min_CurrTableD64.y,min_CurrTableD64.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.z,min_CurrTable.Rq,'r');
title('z - Rq')
text(min_CurrTable.z,min_CurrTable.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.z,min_CurrTableD64.Rq,'b');
title('z - Rq')
text(min_CurrTableD64.z,min_CurrTableD64.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.x,min_CurrTable.Rz,'r');
title('y - Rz')
text(min_CurrTable.x,min_CurrTable.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.x,min_CurrTableD64.Rz,'b')
title('x - Rz')
text(min_CurrTableD64.x,min_CurrTableD64.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.y,min_CurrTable.Rz,'r');
title('y - Rz')
text(min_CurrTable.y,min_CurrTable.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.y,min_CurrTableD64.Rz,'b');
title('y - Rz')
text(min_CurrTableD64.y,min_CurrTableD64.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.z,min_CurrTable.Rz,'r');
title('z - Rz')
text(min_CurrTable.z,min_CurrTable.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.z,min_CurrTableD64.Rz,'b');
title('z - Rz')
text(min_CurrTableD64.z,min_CurrTableD64.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.x,min_CurrTable.Wt,'r');
title('y - Wt')
text(min_CurrTable.x,min_CurrTable.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.x,min_CurrTableD64.Wt,'b')
title('x - Wt')
text(min_CurrTableD64.x,min_CurrTableD64.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.y,min_CurrTable.Wt,'r');
title('y - Wt')
text(min_CurrTable.y,min_CurrTable.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.y,min_CurrTableD64.Wt,'b');
title('y - Wt')
text(min_CurrTableD64.y,min_CurrTableD64.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(min_CurrTable.z,min_CurrTable.Wt,'r');
title('z - Wt')
text(min_CurrTable.z,min_CurrTable.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(min_CurrTableD64.z,min_CurrTableD64.Wt,'b');
title('z - Wt')
text(min_CurrTableD64.z,min_CurrTableD64.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off