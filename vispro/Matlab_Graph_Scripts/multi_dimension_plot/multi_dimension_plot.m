all_SpW_vaLoad=cat(1,SpW_vaLoad,SpWD64_vaLoad);


SpW_vaLoad_normalized =table;
SpW_vaLoad_normalized.x = normalize(all_SpW_vaLoad.x, 'range', [-1 1])
SpW_vaLoad_normalized.y = normalize(all_SpW_vaLoad.y, 'range', [-1 1])
SpW_vaLoad_normalized.z = normalize(all_SpW_vaLoad.z, 'range', [-1 1])
SpW_vaLoad_normalized.Ra = normalize(all_SpW_vaLoad.Ra, 'range', [-1 1])
SpW_vaLoad_normalized.Rq = normalize(all_SpW_vaLoad.Rq, 'range', [-1 1])
SpW_vaLoad_normalized.Rz = normalize(all_SpW_vaLoad.Rz, 'range', [-1 1])
SpW_vaLoad_normalized.Wt = normalize(all_SpW_vaLoad.Wt, 'range', [-1 1])


trans_Table=rows2vars(all_SpW_vaLoad)
% trans_Table=rows2vars(SpW_vaLoad_normalized)


hold on
plot(trans_Table.Var1,'-r*');
plot(trans_Table.Var2,'-r*');
plot(trans_Table.Var3,'-r');
plot(trans_Table.Var4,'-r');
plot(trans_Table.Var5,'--r*');
plot(trans_Table.Var6,'--r*');
plot(trans_Table.Var7,'--r');
plot(trans_Table.Var8,'--r');
plot(trans_Table.Var9,'-b*');
plot(trans_Table.Var10,'-b*');
plot(trans_Table.Var11,'-b');
plot(trans_Table.Var12,'-b');
plot(trans_Table.Var13,'--b*');
plot(trans_Table.Var14,'--b*');
plot(trans_Table.Var15,'--b');
plot(trans_Table.Var16,'--b');
xticklabels(trans_Table.OriginalVariableNames)

h = zeros(3, 1);
h(1) = plot(NaN,NaN,'ob','DisplayName','D64');
h(2) = plot(NaN,NaN,'or','DisplayName','D126');
h(3) = plot(NaN,NaN,'k*','DisplayName','US on');
h(4) = plot(NaN,NaN,'-k','DisplayName','Y-Axis');
h(5) = plot(NaN,NaN,'--k','DisplayName','X-Axis');
legend(h);
hold off
