

tableType='max';
measurementType='vaLoad';

isD64=1;


RaV='Ra';
RqV='Rq';
RzV='Rz';
WtV='Wt';

if isD64==true
    tableType_=append(tableType,'D64');
    RaV_=append(RaV,'D64');
    RqV_=append(RqV,'D64');
    RzV_=append(RzV,'D64');
    WtV_=append(WtV,'D64');
else
    tableType_=tableType;
    RaV_=RaV;
    RqV_=RqV;
    RzV_=RzV;
    WtV_=WtV;
end


eval(append(tableType_,'_',measurementType,'=table'));
eval(append(tableType_,'_',measurementType,'.x=[',tableType_,'_Bearbeitung_Bahn_1_in_Y_mit_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_2_in_Y_mit_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_3_in_Y_ohne_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_4_in_Y_ohne_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_5_in_X_mit_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_6_in_X_mit_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_7_in_X_ohne_US_',measurementType,'X',';',tableType_,'_Bearbeitung_Bahn_8_in_X_ohne_US_',measurementType,'X',']'));
eval(append(tableType_,'_',measurementType,'.y=[',tableType_,'_Bearbeitung_Bahn_1_in_Y_mit_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_2_in_Y_mit_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_3_in_Y_ohne_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_4_in_Y_ohne_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_5_in_X_mit_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_6_in_X_mit_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_7_in_X_ohne_US_',measurementType,'Y',';',tableType_,'_Bearbeitung_Bahn_8_in_X_ohne_US_',measurementType,'Y',']'));
eval(append(tableType_,'_',measurementType,'.z=[',tableType_,'_Bearbeitung_Bahn_1_in_Y_mit_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_2_in_Y_mit_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_3_in_Y_ohne_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_4_in_Y_ohne_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_5_in_X_mit_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_6_in_X_mit_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_7_in_X_ohne_US_',measurementType,'Z',';',tableType_,'_Bearbeitung_Bahn_8_in_X_ohne_US_',measurementType,'Z',']'));
eval(append(tableType_,'_',measurementType,'.Ra=',RaV_));
eval(append(tableType_,'_',measurementType,'.Rq=',RqV_));
eval(append(tableType_,'_',measurementType,'.Rz=',RzV_));
eval(append(tableType_,'_',measurementType,'.Wt=',WtV_));

