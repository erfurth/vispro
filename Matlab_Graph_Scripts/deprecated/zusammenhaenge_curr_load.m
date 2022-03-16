title('D126');
label = string(1:8);
labelOffset=0.005;

tiledlayout(1,3)
nexttile
scatter(tableCurrLoad5.CurrX,tableCurrLoad5.LoadX);

nexttile
scatter(tableCurrLoad5.CurrY,tableCurrLoad5.LoadY);

nexttile
scatter(tableCurrLoad5.CurrZ,tableCurrLoad5.LoadZ);