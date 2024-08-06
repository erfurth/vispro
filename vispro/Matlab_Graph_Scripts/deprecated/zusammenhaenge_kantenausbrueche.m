title('D126');
label = string(1:8);
labelOffset=0.005;

tiledlayout(3,2)
nexttile
scatter(Kantenausbrueche_meanD64_vaLoad.x,Kantenausbrueche_meanD64_vaLoad.kab_gleich,'r');
title('x - Chipped edges in Co-rotation')
xlabel({'Load','in %'});
ylabel({'Chipped edges','in µm²'});
text(Kantenausbrueche_meanD64_vaLoad.x,Kantenausbrueche_meanD64_vaLoad.kab_gleich+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');

nexttile
scatter(Kantenausbrueche_meanD64_vaLoad.x,Kantenausbrueche_meanD64_vaLoad.kab_gegen,'r');
title('x - Chipped edges in Counter-rotation')
xlabel({'Load','in %'});
ylabel({'Chipped edges','in µm²'});
text(Kantenausbrueche_meanD64_vaLoad.x,Kantenausbrueche_meanD64_vaLoad.kab_gegen+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');

nexttile
scatter(Kantenausbrueche_meanD64_vaLoad.y,Kantenausbrueche_meanD64_vaLoad.kab_gleich,'r');
xlabel({'Load','in %'});
ylabel({'Chipped edges','in µm²'});
title('y - Chipped edges in Co-rotation')

text(Kantenausbrueche_meanD64_vaLoad.y,Kantenausbrueche_meanD64_vaLoad.kab_gleich+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');

nexttile
scatter(Kantenausbrueche_meanD64_vaLoad.y,Kantenausbrueche_meanD64_vaLoad.kab_gegen,'r');
title('y - Chipped edges in Counter-rotation')
xlabel({'Load','in %'});
ylabel({'Chipped edges','in µm²'});
text(Kantenausbrueche_meanD64_vaLoad.y,Kantenausbrueche_meanD64_vaLoad.kab_gegen+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');

nexttile
scatter(Kantenausbrueche_meanD64_vaLoad.z,Kantenausbrueche_meanD64_vaLoad.kab_gleich,'r');
title('z - Chipped edges in Co-rotation')
xlabel({'Load','in %'});
ylabel({'Chipped edges','in µm²'});;
text(Kantenausbrueche_meanD64_vaLoad.z,Kantenausbrueche_meanD64_vaLoad.kab_gleich+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');


nexttile
scatter(Kantenausbrueche_meanD64_vaLoad.z,Kantenausbrueche_meanD64_vaLoad.kab_gegen,'r');
title('z - Chipped edges in Counter-rotation')
xlabel({'Load','in %'});
ylabel({'Chipped edges','in µm²'});
text(Kantenausbrueche_meanD64_vaLoad.z,Kantenausbrueche_meanD64_vaLoad.kab_gegen+labelOffset,label,'HorizontalAlignment','center','VerticalAlignment','bottom');


