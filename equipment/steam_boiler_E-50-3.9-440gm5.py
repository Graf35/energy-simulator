import tablreader
import pickle
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import PolynomialFeatures


class Steam_boiler():
    def __int__(self, mode):
        self.K5T4=float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "K5T4", mode))
        self.K5P21=float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "K5P21", mode))
        self.K5T18_2=float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "K5T18_2", mode))
        K5T7=0
        K5P19_1=0
        K5P19_2=0
        K5T8_1=0
        K5T8_2 = 0
        K5T8_3 = 0
        K5P23=0
        K5P24=0
        K5P20=0
        K5P18_1=0
        K5T5_2=0
        K5T5_1=0
        K5T18_1=0
        K5T9_1=0
        K5T9_2 = 0
        K5T10_1 = 0
        K5T10_2 = 0
        K5T8_4 = 0
        K5T8_5 = 0
        K5T8_6 = 0
        K5HCV63_task=0
        K5HCV62_task=0
        K5HCV63=0
        K5HCV62=0
        K5PCV6_task=0
        K5PCV6=0
        K5P6=0
        current_fan=0
        fan=False
        K5PC6CHSP = 0
        K5PC6CHPV = 0
        K5PC6CHOP = 0
        K5PC6CHMO = "M"
        K5PS14_1=0
        K5PS14_2=0
        K5V4=False
        K5L1_1_connection=True
        K5L1_1=-350
        K5L1_1_select=True
        K5L1_2_connection = False
        K5L1_2 = -350
        K5L1_2_select= False
        K5L1_3_connection = False
        K5L1_3 = -350
        K5L1_3_select = False
        K5L1_4_connection = False
        K5L1_4 = -350
        K5L1_4_select = False
        K5P5_1=0
        k5P5_1_select=True
        K5P5_2 = 0
        k5P5_2_select = False
        purge_proved=False
        K5Q3=0
        K5T17=0
        K5V10=False
        K5V7=False
        K5V8=False
        K5T3=0
        K5V9=False
        K5T14=0
        K5V3=False
        K5T6=0
        K5P10=0
        K5T15=0
        K5T16=0
        K5P8=0
        K5T2_1=0
        K5T2_1_select=True
        K5T2_2 = 0
        K5T2_2_select = False
        K5TCV2=0
        K5TCV2_task=0
        K5TCV2_apass=False
        K5TCV2_control="M"
        K5LCV2=0
        K5LCV2_apass = False
        K5TCV1_1 = 0
        K5TCV1_1_task = 0
        K5TCV1_1_apass = False
        K5TCV1_1_control = "M"
        K5TCV1 = 0
        K5TCV1_1_task = 0
        K5TCV1_apass = False
        K5TCV1_control = "M"
        K5V12=False
        K5F11=False
        K5F5=0
        K5L2=0
        K5P13=0
        K5P13_1=0
        K5F6x=0
        K0P102_1=0
        K0T104_2=0
        K5V1=False
        K5V1_control = "M"
        K5V2 = False
        periodic_recharge=False
        K5V5=False
        K5FCV4_1=0
        K5FCV4_1_task = 0
        K5FCV4_1_apass = False
        K5FCV4_1_control = "M"
        K5V6 = False
        K5FCV4_2 = 0
        K5FCV4_2_task = 0
        K5FCV4_2_apass = False
        K5FCV4_2_control = "M"
        K5Q2_1=0
        K5Q2_2=0
        K5P4_1=0
        K5P4_1_select = True
        K5P4_2 = 0
        K5P4_2_select = True
        K5V28=False
        K5HCV53=False
        K5F3=0
        K5T20=0
        K5P110=63
        K5PCV4=0
        K5PCV4_task = 0
        K5PCV4_apass = False
        K5PCV4_control = "M"
        K5P23=0
        K5P24=0
        K5Q3=0
        K5P6_1=0
        K5P6_1_select = True
        K5P6_2 = 0
        K5P6_2_select = False
        K0P125=0
        K5HCV27_1=True
        K5HCV26_1 = True
        K5HCV27_2 = True
        K5HCV26_2 = True
        K5HCV50_1 = False
        K5V51_1 = False
        K5PCV17_1=0
        K5PCV17_1_task=0
        K5P17_1=0
        K5HCV50_2 = False
        K5V51_2 = False
        K5PCV17_2 = 0
        K5PCV17_2_task = 0
        K5P17_2 = 0
        K5HCV50=False
        K5HCV51=False
        igniter_1=False
        igniter_2=False
        burner_1=False
        burner_2=False
        K5P16_1=0
        K5P16_2 = 0
        K5HCV60=0
        K5HCV60_task = 0
        K5HCV61 = 0
        K5HCV61_task = 0
        K5T12=0
        Ksmoke_pump=Smoke_pump(mode)
        KK5PCV5=K5PCV5(mode)

    def change_K5T4(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T4.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.K5PC5CH], 'K5PCV5I.PV': [self.K5PCV5], 'K5T18_2.PV': [self.K5T18_2],
                 'K5PC6CH.OP': [self.K5PC6CH], 'K5T9_2.PV': [self.K5T9_2], 'K5PCV6I.PV': [self.K5PCV6],
                 'K5T10_1.PV': [self.K5T10_1],'K5T10_2.PV': [self.K5T10_2.PV]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T4 = float(model.predict(table_entrance)[0][0])

    def change_K5P21(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P21.sav'), 'rb'))
        entrance = {'K5P18_2.PV': [self.K5P21]}
        table_entrance = pd.DataFrame(data=entrance)
        quadratic = PolynomialFeatures(degree=2)
        self.K5P21 = float(model.predict(quadratic.fit_transform(table_entrance))[0][0])

    def change_K5T18_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T18_2.sav'), 'rb'))
        entrance = {'K5P6.PV':[self.K5P6], 'K5PC5CH.OP':[self.K5T10_1], 'K5T10_2.PV':[self.K5T10_2],
        'K5P23.PV':[self.K5P23], 'K5P24.PV':[self.K5P24], 'K5P20.PV':[self.K5P20], 'K5T5_1.PV':[self.K5T5_1],
        'K5T5_2.PV':[self.K5T5_2], 'K5T8_4.PV':[self.K5T8_4], 'K5T8_5.PV':[self.K5T8_5], 'K5T8_6.PV':[self.K5T8_6]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T18_2 = float(model.predict(table_entrance)[0][0])



class Smoke_pump():
    def __init__(self, mode):
        self.smoke_pump = tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "smoke_pump", mode)
        self.current_smoke_pump = int(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "current_smoke_pump", mode))
        self.K5PC5CHSP = int(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "K5PC5CHSP", mode))
        self.K5PC5CHOP = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "K5PC5CHOP", mode))
        self.K5PC5CHMO = tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "K5PC5CHMO", mode)
        self.K5PC5CHOP_task=float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "K5PC5CHOP", mode))
        self.speed=1.11
    def automatic_adjustment(self, K5PC6CH, K5F3):
        model = pickle.load(open(Path(Path.cwd(), 'models',"model", 'K5PC5HC.sav'), 'rb'))
        entrance = {'K5PC6CH.OP': [K5PC6CH], 'K5F3.PV': [K5F3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5PC5CHOP_task=float(model.predict(table_entrance)[0][0])
        if self.K5PC5CHOP_task>self.K5PC5CHOP:
            self.open()
        elif self.K5PC5CHOP_task<self.K5PC5CHOP:
            self.close()

    def mechanic_adjustment(self, K5PC5CHOP_task):
        self.K5PC5CHOP_task=K5PC5CHOP_task #пробросить число от пользователя
        if self.K5PC5CHOP_task>self.K5PC5CHOP:
            self.open()
        elif self.K5PC5CHOP_task<self.K5PC5CHOP:
            self.close()

    def open(self):
        if self.K5PC5CHOP+self.speed>=self.K5PC5CHOP_task:
            self.K5PC5CHOP=self.K5PC5CHOP_task
        else:
            self.K5PC5CHOP+=self.speed
    def close(self):
        if self.K5PC5CHOP-self.speed<=self.K5PC5CHOP_task:
            self.K5PC5CHOP=self.K5PC5CHOP_task
        else:
            self.K5PC5CHOP-=self.speed

class K5PCV5():
    def __init__(self, mode):
        self.K5PCV5_task = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "K5PCV5_task", mode))
        self.K5PCV5 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'),"объект", "K5PCV5", mode))
        self.speed = 1.11

    def mechanic_adjustment(self, K5PCV5_task):
        self.K5PC5CHOP_task=K5PCV5_task #пробросить число от пользователя
        if self.K5PCV5_task>self.K5PCV5:
            self.open()
        elif self.K5PCV5_task<self.K5PCV5:
            self.close()

    def open(self):
        if self.K5PCV5+self.speed>=self.K5PCV5_task:
            self.K5PCV5=self.K5PCV5_task
        else:
            self.K5PCV5+=self.speed
    def close(self):
        if self.K5PCV5-self.speed<=self.K5PCV5_task:
            self.K5PCV5=self.K5PCV5_task
        else:
            self.K5PCV5-=self.speed


