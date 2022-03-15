
tableName='Kantenausbrueche';
tableType='mean';
measurementType='vaLoad';

isD64=true;


kab_gegen='Kantenausbrueche_Gegenlauf';
kab_gleich='Kantenausbrueche_Gleichlauf';

if isD64==true
    tableType_=append(tableType,'D64');
    kab_gegen_=append(kab_gegen,'D64');
    kab_gleich_=append(kab_gleich,'D64');
else
    tableType_=tableType;
    kab_gegen_=kab_gegen;
    kab_gleich_=kab_gleich;
end

eval(append(tableName,'_',tableType_,'_',measurementType,'=table'));
eval(append(tableName,'_',tableType_,'_',measurementType,'.x=[',tableType_,'_Bearbeitung_Bahn_1_in_Y_mit_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_2_in_Y_mit_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_3_in_Y_ohne_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_4_in_Y_ohne_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_5_in_X_mit_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_6_in_X_mit_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_7_in_X_ohne_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_8_in_X_ohne_US_',measurementType,'X',']'));
eval(append(tableName,'_',tableType_,'_',measurementType,'.y=[',tableType_,'_Bearbeitung_Bahn_1_in_Y_mit_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_2_in_Y_mit_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_3_in_Y_ohne_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_4_in_Y_ohne_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_5_in_X_mit_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_6_in_X_mit_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_7_in_X_ohne_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_8_in_X_ohne_US_',measurementType,'Y',']'));
eval(append(tableName,'_',tableType_,'_',measurementType,'.z=[',tableType_,'_Bearbeitung_Bahn_1_in_Y_mit_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_2_in_Y_mit_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_3_in_Y_ohne_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_4_in_Y_ohne_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_5_in_X_mit_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_6_in_X_mit_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_7_in_X_ohne_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_8_in_X_ohne_US_',measurementType,'Z',']'));
eval(append(tableName,'_',tableType_,'_',measurementType,'.kab_gleich=',kab_gleich_));
eval(append(tableName,'_',tableType_,'_',measurementType,'.kab_gegen=',kab_gegen_));


