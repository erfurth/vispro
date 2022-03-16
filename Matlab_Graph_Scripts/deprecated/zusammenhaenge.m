title('D64');
label = string(1:8);
labelOffset=0.005;

tiledlayout(4,3)
nexttile
scatter(meanLoadTable.x,meanLoadTable.Ra,'r');
title('y - Ra')
text(meanLoadTable.x,meanLoadTable.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.x,meanLoadTableD64.Ra,'b')
title('x - Ra')
text(meanLoadTableD64.x,meanLoadTableD64.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.y,meanLoadTable.Ra,'r');
title('y - Ra')
text(meanLoadTable.y,meanLoadTable.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.y,meanLoadTableD64.Ra,'b');
title('y - Ra')
text(meanLoadTableD64.y,meanLoadTableD64.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.z,meanLoadTable.Ra,'r');
title('z - Ra')
text(meanLoadTable.z,meanLoadTable.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.z,meanLoadTableD64.Ra,'b');
title('z - Ra')
text(meanLoadTableD64.z,meanLoadTableD64.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.x,meanLoadTable.Rq,'r');
title('y - Rq')
text(meanLoadTable.x,meanLoadTable.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.x,meanLoadTableD64.Rq,'b')
title('x - Rq')
text(meanLoadTableD64.x,meanLoadTableD64.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.y,meanLoadTable.Rq,'r');
title('y - Rq')
text(meanLoadTable.y,meanLoadTable.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.y,meanLoadTableD64.Rq,'b');
title('y - Rq')
text(meanLoadTableD64.y,meanLoadTableD64.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.z,meanLoadTable.Rq,'r');
title('z - Rq')
text(meanLoadTable.z,meanLoadTable.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.z,meanLoadTableD64.Rq,'b');
title('z - Rq')
text(meanLoadTableD64.z,meanLoadTableD64.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.x,meanLoadTable.Rz,'r');
title('y - Rz')
text(meanLoadTable.x,meanLoadTable.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.x,meanLoadTableD64.Rz,'b')
title('x - Rz')
text(meanLoadTableD64.x,meanLoadTableD64.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.y,meanLoadTable.Rz,'r');
title('y - Rz')
text(meanLoadTable.y,meanLoadTable.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.y,meanLoadTableD64.Rz,'b');
title('y - Rz')
text(meanLoadTableD64.y,meanLoadTableD64.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.z,meanLoadTable.Rz,'r');
title('z - Rz')
text(meanLoadTable.z,meanLoadTable.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.z,meanLoadTableD64.Rz,'b');
title('z - Rz')
text(meanLoadTableD64.z,meanLoadTableD64.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.x,meanLoadTable.Wt,'r');
title('y - Wt')
text(meanLoadTable.x,meanLoadTable.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.x,meanLoadTableD64.Wt,'b')
title('x - Wt')
text(meanLoadTableD64.x,meanLoadTableD64.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.y,meanLoadTable.Wt,'r');
title('y - Wt')
text(meanLoadTable.y,meanLoadTable.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.y,meanLoadTableD64.Wt,'b');
title('y - Wt')
text(meanLoadTableD64.y,meanLoadTableD64.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(meanLoadTable.z,meanLoadTable.Wt,'r');
title('z - Wt')
text(meanLoadTable.z,meanLoadTable.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanLoadTableD64.z,meanLoadTableD64.Wt,'b');
title('z - Wt')
text(meanLoadTableD64.z,meanLoadTableD64.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off