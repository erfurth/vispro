title('D126');
label = string(1:8);
labelOffset=0.005;

tiledlayout(4,3)
nexttile
scatter(max_LoadTable.x,max_LoadTable.Ra,'r');
title('y - Ra')
text(max_LoadTable.x,max_LoadTable.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.x,max_LoadTableD64.Ra,'b')
title('x - Ra')
text(max_LoadTableD64.x,max_LoadTableD64.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.y,max_LoadTable.Ra,'r');
title('y - Ra')
text(max_LoadTable.y,max_LoadTable.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.y,max_LoadTableD64.Ra,'b');
title('y - Ra')
text(max_LoadTableD64.y,max_LoadTableD64.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.z,max_LoadTable.Ra,'r');
title('z - Ra')
text(max_LoadTable.z,max_LoadTable.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.z,max_LoadTableD64.Ra,'b');
title('z - Ra')
text(max_LoadTableD64.z,max_LoadTableD64.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.x,max_LoadTable.Rq,'r');
title('y - Rq')
text(max_LoadTable.x,max_LoadTable.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.x,max_LoadTableD64.Rq,'b')
title('x - Rq')
text(max_LoadTableD64.x,max_LoadTableD64.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.y,max_LoadTable.Rq,'r');
title('y - Rq')
text(max_LoadTable.y,max_LoadTable.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.y,max_LoadTableD64.Rq,'b');
title('y - Rq')
text(max_LoadTableD64.y,max_LoadTableD64.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.z,max_LoadTable.Rq,'r');
title('z - Rq')
text(max_LoadTable.z,max_LoadTable.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.z,max_LoadTableD64.Rq,'b');
title('z - Rq')
text(max_LoadTableD64.z,max_LoadTableD64.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.x,max_LoadTable.Rz,'r');
title('y - Rz')
text(max_LoadTable.x,max_LoadTable.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.x,max_LoadTableD64.Rz,'b')
title('x - Rz')
text(max_LoadTableD64.x,max_LoadTableD64.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.y,max_LoadTable.Rz,'r');
title('y - Rz')
text(max_LoadTable.y,max_LoadTable.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.y,max_LoadTableD64.Rz,'b');
title('y - Rz')
text(max_LoadTableD64.y,max_LoadTableD64.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.z,max_LoadTable.Rz,'r');
title('z - Rz')
text(max_LoadTable.z,max_LoadTable.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.z,max_LoadTableD64.Rz,'b');
title('z - Rz')
text(max_LoadTableD64.z,max_LoadTableD64.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.x,max_LoadTable.Wt,'r');
title('y - Wt')
text(max_LoadTable.x,max_LoadTable.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.x,max_LoadTableD64.Wt,'b')
title('x - Wt')
text(max_LoadTableD64.x,max_LoadTableD64.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.y,max_LoadTable.Wt,'r');
title('y - Wt')
text(max_LoadTable.y,max_LoadTable.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.y,max_LoadTableD64.Wt,'b');
title('y - Wt')
text(max_LoadTableD64.y,max_LoadTableD64.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off

nexttile
scatter(max_LoadTable.z,max_LoadTable.Wt,'r');
title('z - Wt')
text(max_LoadTable.z,max_LoadTable.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(max_LoadTableD64.z,max_LoadTableD64.Wt,'b');
title('z - Wt')
text(max_LoadTableD64.z,max_LoadTableD64.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold off