import tablreader
import pickle
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import PolynomialFeatures


class Steam_boiler():
    def __int__(self, mode):
        self.K5T4 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T4", mode))
        self.K5P21 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P21", mode))
        self.K5T18_2 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T18_2", mode))
        self.K5T7 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T7", mode))
        self.K5P19_1 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P19_1", mode))
        self.K5P19_2 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P19_2", mode))
        self.K5T8_1 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_1", mode))
        self.K5T8_2 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_2", mode))
        self.K5T8_3 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_3", mode))
        self.K5P23 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P23", mode))
        self.K5P24 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5TP24", mode))
        self.K5P20 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5TP20", mode))
        self.K5P18_1 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P18_1", mode))
        self.K5P18_2 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P18_2", mode))
        self.K5T5_2 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T5_2", mode))
        self.K5T5_1 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T5_1", mode))
        self.K5T18_1 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T18_1", mode))
        self.K5T9_2 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T9_2", mode))
        self.K5T9_1 = self.K5T9_2
        self.K5T10_1 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T10_1", mode))
        self.K5T10_2 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T10_2", mode))
        self.K5T8_4 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_4", mode))
        self.K5T8_5 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_5", mode))
        self.K5T8_6 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_6", mode))
        self.K5PS14_1 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PS14_1", mode))
        self.K5PS14_2 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PS14_2", mode))
        self.K5V4 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5V4", mode))
        self.K5L1_1_connection =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_1_connection", mode))
        self.K5L1_1 =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_1", mode))
        self.K5L1_1_select =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_1_select", mode))
        self.K5L1_2_connection =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_2_connection", mode))
        self.K5L1_2 =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_2", mode))
        self.K5L1_2_select =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_2_select", mode))
        self.K5L1_3_connection =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_3_connection", mode))
        self.K5L1_3= float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_3", mode))
        self.K5L1_3_select =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_3_select", mode))
        self.K5L1_4_connection =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_4_connection", mode))
        self.K5L1_4 =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_4", mode))
        self.K5L1_4_select =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_4_select", mode))
        self.K5P5_1 =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P5_1", mode))
        self.k5P5_1_select =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "k5P5_1_select", mode))
        self.K5P5_2 =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P5_2", mode))
        self.K5P5_2_select =float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P5_2_select", mode))
        purge_proved = False
        K5Q3 = 0
        K5T17 = 0
        K5V10 = False
        K5V7 = False
        K5V8 = False
        K5T3 = 0
        K5V9 = False
        K5T14 = 0
        K5V3 = False
        K5T6 = 0
        K5P10 = 0
        K5T15 = 0
        K5T16 = 0
        K5P8 = 0
        K5T2_1 = 0
        K5T2_1_select = True
        K5T2_2 = 0
        K5T2_2_select = False
        K5TCV2 = 0
        K5TCV2_task = 0
        K5TCV2_apass = False
        K5TCV2_control = "M"
        K5LCV2 = 0
        K5LCV2_apass = False
        K5TCV1_1 = 0
        K5TCV1_1_task = 0
        K5TCV1_1_apass = False
        K5TCV1_1_control = "M"
        K5TCV1 = 0
        K5TCV1_1_task = 0
        K5TCV1_apass = False
        K5TCV1_control = "M"
        K5V12 = False
        K5F11 = False
        K5F5 = 0
        K5L2 = 0
        K5P13 = 0
        K5P13_1 = 0
        K5F6x = 0
        K0P102_1 = 0
        K0T104_2 = 0
        K5V1 = False
        K5V1_control = "M"
        K5V2 = False
        periodic_recharge = False
        K5V5 = False
        K5FCV4_1 = 0
        K5FCV4_1_task = 0
        K5FCV4_1_apass = False
        K5FCV4_1_control = "M"
        K5V6 = False
        K5FCV4_2 = 0
        K5FCV4_2_task = 0
        K5FCV4_2_apass = False
        K5FCV4_2_control = "M"
        K5Q2_1 = 0
        K5Q2_2 = 0
        K5P4_1 = 0
        K5P4_1_select = True
        K5P4_2 = 0
        K5P4_2_select = True
        K5V28 = False
        K5HCV53 = False
        K5F3 = 0
        K5T20 = 0
        K5P110 = 63
        K5PCV4 = 0
        K5PCV4_task = 0
        K5PCV4_apass = False
        K5PCV4_control = "M"
        K5P23 = 0
        K5P24 = 0
        K5Q3 = 0
        K5P6_1 = 0
        K5P6_1_select = True
        K5P6_2 = 0
        K5P6_2_select = False
        K0P125 = 0
        K5HCV27_1 = True
        K5HCV26_1 = True
        K5HCV27_2 = True
        K5HCV26_2 = True
        K5HCV50_1 = False
        K5V51_1 = False
        K5PCV17_1 = 0
        K5PCV17_1_task = 0
        K5P17_1 = 0
        K5HCV50_2 = False
        K5V51_2 = False
        K5PCV17_2 = 0
        K5PCV17_2_task = 0
        K5P17_2 = 0
        K5HCV50 = False
        K5HCV51 = False
        igniter_1 = False
        igniter_2 = False
        burner_1 = False
        burner_2 = False
        K5P16_1 = 0
        K5P16_2 = 0
        K5HCV60 = 0
        K5HCV60_task = 0
        K5HCV61 = 0
        K5HCV61_task = 0
        K5T12 = 0
        self.Ksmoke_pump = Smoke_pump(mode)
        self.KK5PCV5 = K5PCV5(mode)
        self.KK5HCV62 = K5HCV62(mode)
        self.KK5HCV63 = K5HCV63(mode)
        self.fun=Fan(mode)

    def change_K5T4(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T4.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5PCV5I.PV': [self.K5PCV5],
                    'K5T18_2.PV': [self.K5T18_2],
                    'K5PC6CH.OP': [self.K5PC6CH], 'K5T9_2.PV': [self.K5T9_2], 'K5PCV6I.PV': [self.K5PCV6],
                    'K5T10_1.PV': [self.K5T10_1], 'K5T10_2.PV': [self.K5T10_2.PV]}
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
        entrance = {'K5P6.PV': [self.K5P6], 'K5PC5CH.OP': [self.K5T10_1], 'K5T10_2.PV': [self.K5T10_2],
                    'K5P23.PV': [self.K5P23], 'K5P24.PV': [self.K5P24], 'K5P20.PV': [self.K5P20],
                    'K5T5_1.PV': [self.K5T5_1],
                    'K5T5_2.PV': [self.K5T5_2], 'K5T8_4.PV': [self.K5T8_4], 'K5T8_5.PV': [self.K5T8_5],
                    'K5T8_6.PV': [self.K5T8_6]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T18_2 = float(model.predict(table_entrance)[0][0])

    def change_K5T7(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T7.sav'), 'rb'))
        entrance = {'K5T8_1.PV': [self.K5T8_1]}
        table_entrance = pd.DataFrame(data=entrance)
        quadratic = PolynomialFeatures(degree=2)
        self.K5T7 = float(model.predict(quadratic.fit_transform(table_entrance))[0][0])

    def change_K5P19_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P19_1.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5PC6CH.OP': [self.K5PC6CH]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P19_1 = float(model.predict(table_entrance)[0][0])

    def change_K5P19_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P19_2.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5PC6CH.OP': [self.K5PC6CH]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P19_2 = float(model.predict(table_entrance)[0][0])

    def change_K5T8_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T8_1.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5T4.PV': [self.K5T4],
                    'K5T7.PV': [self.K5T7], 'K5PC6CH.OP': [self.K5PC6CH], 'K5T9_2.PV': [self.K5T9_2]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T8_1 = float(model.predict(table_entrance)[0][0])

    def change_K5T8_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T8_2.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5T4.PV': [self.K5T4],
                    'K5T7.PV': [self.K5T7], 'K5PC6CH.OP': [self.K5PC6CH]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T8_2 = float(model.predict(table_entrance)[0][0])

    def change_K5T8_3(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T8_3.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5T4.PV': [self.K5T4],
                    'K5T7.PV': [self.K5T7], 'K5PC6CH.OP': [self.K5PC6CH]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T8_3 = float(model.predict(table_entrance)[0][0])

    def change_K5P23(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P23.sav'), 'rb'))
        entrance = {'K5P6.PV':[self.K5P6], 'K5PCV6I.PV':[self.K5PCV6I], 'K5PC6CH.OP': [self.K5PC6CH]}
        table_entrance = pd.DataFrame(data=entrance)
        quadratic = PolynomialFeatures(degree=2)
        self.K5P23 = float(model.predict(quadratic.fit_transform(table_entrance))[0][0])

    def change_K5P24(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P24.sav'), 'rb'))
        entrance = {'K5P6.PV':[self.K5P6], 'K5PCV6I.PV':[self.K5PCV6I], 'K5PC6CH.OP': [self.K5PC6CH]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P24 = float(model.predict(table_entrance)[0][0])

    def change_K5P20(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P20.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP]}
        table_entrance = pd.DataFrame(data=entrance)
        quadratic = PolynomialFeatures(degree=2)
        self.K5P20 = float(model.predict(quadratic.fit_transform(table_entrance))[0][0])

    def change_K5P18_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P18_1.sav'), 'rb'))
        entrance = {'K0P125.PV': [self.K0P125]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P18_1 = float(model.predict(table_entrance)[0][0])

    def change_K5P18_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P18_2.sav'), 'rb'))
        entrance = {'K0P125.PV': [self.K0P125]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P18_2 = float(model.predict(table_entrance)[0][0])

    def change_K5T5_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T5_1.sav'), 'rb'))
        entrance = {'K0P125.PV': [self.K0P125], 'K5F3.PV': [self.K5F3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T5_1 = float(model.predict(table_entrance)[0][0])

    def change_K5T5_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T5_2.sav'), 'rb'))
        entrance = {'K0P125.PV': [self.K0P125], 'K5F3.PV': [self.K5F3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T5_2 = float(model.predict(table_entrance)[0][0])

    def change_K5T18_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T18_1.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP],'K5T5_2.PV': [self.K5T5_2],
                    'K5F3.PV': [self.K5F3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T18_1 = float(model.predict(table_entrance)[0][0])

    def change_K5T9_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P9_2.sav'), 'rb'))
        entrance = {'K5T7.PV': [self.K5T7]}
        table_entrance = pd.DataFrame(data=entrance)
        quadratic = PolynomialFeatures(degree=3)
        self.K5T9_2 = float(model.predict(quadratic.fit_transform(table_entrance))[0][0])
        self.K5T9_1=self.K5T9_2

    def change_K5T10_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T10_1.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5T4.PV': [self.K5T4],
                    'K5T18_2.PV': [self.K5T18_2], 'K5PC6CH.OP': [self.K5PC6CH],
                    'K5T8_3.PV': [self.K5T8_3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T10_1 = float(model.predict(table_entrance)[0][0])

    def change_K5T10_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T10_2.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5T4.PV': [self.K5T4],
                    'K5T18_2.PV': [self.K5T18_2], 'K5PC6CH.OP': [self.K5PC6CH],
                    'K5T8_3.PV': [self.K5T8_3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T10_2 = float(model.predict(table_entrance)[0][0])

    def change_K5T8_4(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T8_4.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5PC6CH.OP': [self.K5PC6CH],
                    'K5T10_2.PV': [self.K5T10_2], 'K5T5_1.PV': [self.K5T5_1],
                    'K5T18_1.PV': [self.K5T18_1], 'K5T12.PV': [self.K5T12],}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T8_4 = float(model.predict(table_entrance)[0][0])

    def change_K5T8_5(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T8_5.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5PC6CH.OP': [self.K5PC6CH],
                    'K5T10_2.PV': [self.K5T10_2], 'K5T5_1.PV': [self.K5T5_1],
                    'K5T18_1.PV': [self.K5T18_1], 'K5T12.PV': [self.K5T12],}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T8_5 = float(model.predict(table_entrance)[0][0])

    def change_K5T8_6(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T8_6.sav'), 'rb'))
        entrance = {'K5PC5CH.OP': [self.Ksmoke_pump.K5PC5CHOP], 'K5PC6CH.OP': [self.K5PC6CH],
                    'K5T10_2.PV': [self.K5T10_2], 'K5T5_1.PV': [self.K5T5_1],
                    'K5T18_1.PV': [self.K5T18_1], 'K5T12.PV': [self.K5T12]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T8_6 = float(model.predict(table_entrance)[0][0])

    def change_K5PS14_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5PS14_1.sav'), 'rb'))
        entrance = {'K5P10.PV': [self.K5P10.PV]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5PSV14_1 = float(model.predict(table_entrance)[0][0])

    def change_K5PS14_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5PS14_2.sav'), 'rb'))
        entrance = {'K5P10.PV': [self.K5P10]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5PSV14_2 = float(model.predict(table_entrance)[0][0])

    def change_K5V4(self):
        if self.K5V4==True:
            self.K5V4=False
        else:
            self.K5V4=True

    def change_K5L1_1_connection(self):
        if self.K5L1_1_connection==True:
            self.K5L1_1_connection=False
        else:
            self.K5L1_1_connection=True

    def change_K5L1_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5L1_1.sav'), 'rb'))
        entrance = {'K5F5.PV': [self.K5F5], 'K5F6X.PV': [self.K5F6X],}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5L1_1 = float(model.predict(table_entrance)[0][0])

    def change_K5L1_1_select(self):
        self.K5L1_1_select=True
        self.K5L1_2_select = False
        self.K5L1_3_select = False
        self.K5L1_4_select = False

    def change_K5L1_2_connection(self):
        if self.K5L1_2_connection == True:
            self.K5L1_2_connection = False
        else:
            self.K5L1_2_connection = True

    def change_K5L1_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5L1_2.sav'), 'rb'))
        entrance = {'K5F5.PV': [self.K5F5], 'K5F6X.PV': [self.K5F6X], }
        table_entrance = pd.DataFrame(data=entrance)
        self.K5L1_2 = float(model.predict(table_entrance)[0][0])

    def change_K5L1_2_select(self):
        self.K5L1_1_select = False
        self.K5L1_2_select = True
        self.K5L1_3_select = False
        self.K5L1_4_select = False

    def change_K5L1_3_connection(self):
        if self.K5L1_3_connection == True:
            self.K5L1_3_connection = False
        else:
            self.K5L1_3_connection = True

    def change_K5L1_3(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5L1_3.sav'), 'rb'))
        entrance = {'K5F5.PV': [self.K5F5], 'K5F6X.PV': [self.K5F6X], }
        table_entrance = pd.DataFrame(data=entrance)
        self.K5L1_3 = float(model.predict(table_entrance)[0][0])

    def change_K5L1_3_select(self):
        self.K5L1_1_select = False
        self.K5L1_2_select = False
        self.K5L1_3_select = True
        self.K5L1_4_select = False

    def change_K5L1_4_connection(self):
        if self.K5L1_4_connection == True:
            self.K5L1_4_connection = False
        else:
            self.K5L1_4_connection = True

    def change_K5L1_4(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5L1_4.sav'), 'rb'))
        entrance = {'K5F5.PV': [self.K5F5], 'K5F6X.PV': [self.K5F6X], }
        table_entrance = pd.DataFrame(data=entrance)
        self.K5L1_4 = float(model.predict(table_entrance)[0][0])

    def change_K5L1_4_select(self):
        self.K5L1_1_select = False
        self.K5L1_2_select = False
        self.K5L1_3_select = False
        self.K5L1_4_select = True

    def change_K5P5_1_select(self):
        self.K5P5_1_select = True
        self.K5P5_2_select = False

    def change_K5P5_2_select(self):
        self.K5P5_1_select = False
        self.K5P5_2_select = True

# TODO:Переобучит сеть в K5P5 на зависимость входа от выхода. Если есть отлисчие от текущего изменять разряжение


class Smoke_pump():
    def __init__(self, mode):
        self.smoke_pump = tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "smoke_pump", mode)
        self.current_smoke_pump = int(
            tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "current_smoke_pump", mode))
        self.K5PC5CHSP = int(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PC5CHSP", mode))
        self.K5PC5CHOP = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PC5CHOP", mode))
        self.K5PC5CHMO = tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PC5CHMO", mode)
        self.K5PC5CHOP_task = float(
            tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PC5CHOP", mode))
        self.speed = 1.11

    def automatic_adjustment(self, K5PC6CH, K5F3):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5PC5HC.sav'), 'rb'))
        entrance = {'K5PC6CH.OP': [K5PC6CH], 'K5F3.PV': [K5F3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5PC5CHOP_task = float(model.predict(table_entrance)[0][0])
        if self.K5PC5CHOP_task > self.K5PC5CHOP:
            self.open()
        elif self.K5PC5CHOP_task < self.K5PC5CHOP:
            self.close()

    def mechanic_adjustment(self, K5PC5CHOP_task):
        self.K5PC5CHOP_task = K5PC5CHOP_task  # пробросить число от пользователя
        if self.K5PC5CHOP_task > self.K5PC5CHOP:
            self.open()
        elif self.K5PC5CHOP_task < self.K5PC5CHOP:
            self.close()

    def open(self):
        if self.K5PC5CHOP + self.speed >= self.K5PC5CHOP_task:
            self.K5PC5CHOP = self.K5PC5CHOP_task
        else:
            self.K5PC5CHOP += self.speed
    def close(self):
        if self.K5PC5CHOP - self.speed <= self.K5PC5CHOP_task:
            self.K5PC5CHOP = self.K5PC5CHOP_task
        else:
            self.K5PC5CHOP -= self.speed


class K5PCV5():
    def __init__(self, mode):
        self.K5PCV5_task = float(
            tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV5_task", mode))
        self.K5PCV5 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV5", mode))
        self.speed = 1.11

    def mechanic_adjustment(self, K5PCV5_task):
        self.K5PC5_task = K5PCV5_task  # пробросить число от пользователя
        if self.K5PCV5_task > self.K5PCV5:
            self.open()
        elif self.K5PCV5_task < self.K5PCV5:
            self.close()

    def open(self):
        if self.K5PCV5 + self.speed >= self.K5PCV5_task:
            self.K5PCV5 = self.K5PCV5_task
        else:
            self.K5PCV5 += self.speed

    def close(self):
        if self.K5PCV5 - self.speed <= self.K5PCV5_task:
            self.K5PCV5 = self.K5PCV5_task
        else:
            self.K5PCV5 -= self.speed

class K5HCV63():
    def __init__(self, mode):
        self.K5HCV63_task = float(
            tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5HCV63_task", mode))
        self.K5HCV63 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV5", mode))
        self.speed = 1.11

    def mechanic_adjustment(self, K5HCV63_task):
        self.K5HCV63_task = K5HCV63_task  # пробросить число от пользователя
        if self.K5HCV63_task > self.K5HCV63:
            self.open()
        elif self.K5HCV63_task < self.K5HCV63:
            self.close()

    def open(self):
        if self.K5HCV63 + self.speed >= self.K5HCV63_task:
            self.K5HCV63 = self.K5HCV63_task
        else:
            self.K5HCV63 += self.speed

    def close(self):
        if self.K5HCV63 - self.speed <= self.K5HCV63_task:
            self.K5HCV63 = self.K5HCV63_task
        else:
            self.K5HCV63 -= self.speed

class K5HCV62():
    def __init__(self, mode):
        self.K5HCV62_task = float(
            tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5HCV62_task", mode))
        self.K5HCV62 = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV5", mode))
        self.speed = 1.11

    def mechanic_adjustment(self, K5HCV63_task):
        self.K5HCV62_task = K5HCV63_task  # пробросить число от пользователя
        if self.K5HCV62_task > self.K5HCV62:
            self.open()
        elif self.K5HCV62_task < self.K5HCV62:
            self.close()

    def open(self):
        if self.K5HCV62 + self.speed >= self.K5HCV62_task:
            self.K5HCV62 = self.K5HCV62_task
        else:
            self.K5HCV62 += self.speed

    def close(self):
        if self.K5HCV62 - self.speed <= self.K5HCV62_task:
            self.K5HCV62 = self.K5HCV62_task
        else:
            self.K5HCV62 -= self.speed

class Fan():
    def __init__(self, mode):
        self.fun = tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "fun", mode)
        self.current_fun = int(
            tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "current_fun", mode))
        self.K5PCV6CHSP = int(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV6CHSP", mode))
        self.K5PCV6CHOP = float(tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV6CHOP", mode))
        self.K5PCV6CHMO = tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV6CHMO", mode)
        self.K5PCV6CHOP_task = float(
            tablreader.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV65CHOP", mode))
        self.speed = 1.11

    def automatic_adjustment(self, K5PCV6CH, K5F3):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5PCV6HC.sav'), 'rb'))
        entrance = {'K5PC6CH.OP': [K5PCV6CH], 'K5F3.PV': [K5F3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5PCV6CHOP_task = float(model.predict(table_entrance)[0][0])
        if self.K5PCV6CHOP_task > self.K5PCV6CHOP:
            self.open()
        elif self.K5PCV6CHOP_task < self.K5PCV6CHOP:
            self.close()

    def mechanic_adjustment(self, K5PCV6CHOP_task):
        self.K5PCV6CHOP_task = K5PCV6CHOP_task  # пробросить число от пользователя
        if self.K5PCV6CHOP_task > self.K5PCV6CHOP:
            self.open()
        elif self.K5PCV6CHOP_task < self.K5PCV6CHOP:
            self.close()
    def open(self):
        if self.K5PCV6CHOP + self.speed >= self.K5PCV6CHOP_task:
            self.K5PCV6CHOP = self.K5PCV6CHOP_task
        else:
            self.K5PCV6CHOP += self.speed
    def close(self):
        if self.K5PCV6CHOP - self.speed <= self.K5PCV6CHOP_task:
            self.K5PCV6CHOP = self.K5PCV6CHOP_task
        else:
            self.K5PCV6CHOP -= self.speed