title('D126');
label = string(1:8);
labelOffset=0.005;

tiledlayout(4,1)
nexttile
scatter(mean_vaLoad.x+mean_vaLoad.y+mean_vaLoad.z+mean_vaLoad.y+mean_vaLoad.z,mean_vaLoad.Ra,'r');
text(mean_vaLoad.x+mean_vaLoad.y+mean_vaLoad.z+mean_vaLoad.y+mean_vaLoad.z,mean_vaLoad.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(mean_vaLoad.x+mean_vaLoad.y+mean_vaLoad.z+mean_vaLoad.y+mean_vaLoad.z,meanD64_vaLoad.Ra,'b')
title('Load - Ra',corr(cat(1,mean_vaLoad.x,meanD64_vaLoad.x)))
text(mean_vaLoad.x+mean_vaLoad.y+mean_vaLoad.z+mean_vaLoad.y+mean_vaLoad.z,meanD64_vaLoad.Ra+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
xlabel({'Load','in %'});
ylabel({'Roughness','in µm²'});
hold off



nexttile
scatter(mean_vaLoad.x+mean_vaLoad.y+mean_vaLoad.z,mean_vaLoad.Rq,'r');
title('Load - Rq')
text(mean_vaLoad.x+mean_vaLoad.y+mean_vaLoad.z,mean_vaLoad.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanD64_vaLoad.x+meanD64_vaLoad.y+meanD64_vaLoad.z,meanD64_vaLoad.Rq,'b')
title('Load - Rq')
text(meanD64_vaLoad.x+meanD64_vaLoad.y+meanD64_vaLoad.z,meanD64_vaLoad.Rq+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
xlabel({'Load','in %'});
ylabel({'Roughness','in µm²'});
hold off



nexttile
scatter(mean_vaLoad.x+mean_vaLoad.y+mean_vaLoad.z,mean_vaLoad.Rz,'r');
title('Load - Rz')
text(mean_vaLoad.x+mean_vaLoad.y+mean_vaLoad.z,mean_vaLoad.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanD64_vaLoad.x+meanD64_vaLoad.y+meanD64_vaLoad.z,meanD64_vaLoad.Rz,'b')
title('Load - Rz')
text(meanD64_vaLoad.x+meanD64_vaLoad.y+meanD64_vaLoad.z,meanD64_vaLoad.Rz+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
xlabel({'Load','in %'});
ylabel({'Roughness','in µm²'});
hold off



nexttile
scatter(mean_vaLoad.x+mean_vaLoad.y+mean_vaLoad.z,mean_vaLoad.Wt,'r');
title('Load - Wt')
text(mean_vaLoad.x+mean_vaLoad.y+mean_vaLoad.z,mean_vaLoad.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
hold on
scatter(meanD64_vaLoad.x+meanD64_vaLoad.y+meanD64_vaLoad.z,meanD64_vaLoad.Wt,'b')
title('Load - Wt')
text(meanD64_vaLoad.x+meanD64_vaLoad.y+meanD64_vaLoad.z,meanD64_vaLoad.Wt+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');
xlabel({'Load','in %'});
ylabel({'Roughness','in µm²'});
hold off

