import Scripts
import pickle
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import PolynomialFeatures
# from gpiozero import PWMOutputDevice
# from gpiozero.pins.pigpio import PiGPIOFactory
# import control
# from control.matlab import *
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import MultiTaskLassoCV
from sklearn.linear_model import Ridge
from sklearn.linear_model import _base
import seaborn as sns
from sklearn import linear_model
from scipy.stats import norm
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score
import Scripts
import scipy.integrate as spi

class Steam_boiler():

    def __init__(self, mode):
        self.K5T4 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T4", mode))
        self.K5P21 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P21", mode))
        self.K5T18_2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T18_2", mode))
        self.K5T7 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T7", mode))
        self.K5P19_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P19_1", mode))
        self.K5P19_2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P19_2", mode))
        self.K5T8_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_1", mode))
        self.K5T8_2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_2", mode))
        self.K5T8_3 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_3", mode))
        self.K5P23 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P23", mode))
        self.K5P24 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P24", mode))
        self.K5P20 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P20", mode))
        self.K5P18_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P18_1", mode))
        self.K5P18_2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P18_2", mode))
        self.K5T5_2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T5_2", mode))
        self.K5T5_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T5_1", mode))
        self.K5T18_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T18_1", mode))
        self.K5T9_2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T9_2", mode))
        self.K5T9_1 = self.K5T9_2
        self.K5T10_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T10_1", mode))
        self.K5T10_2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T10_2", mode))
        self.K5T8_4 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_4", mode))
        self.K5T8_5 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_5", mode))
        self.K5T8_6 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T8_6", mode))
        self.K5PS14_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PS14_1", mode))
        self.K5PS14_2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PS14_2", mode))
        self.K5V4 = bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5V4", mode))
        self.K5L1_1_connection =bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_1_connection", mode))
        self.K5L1_1 =float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_1", mode))
        self.K5L1_1_select =bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_1_select", mode))
        self.K5L1_2_connection =bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_2_connection", mode))
        self.K5L1_2 =float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_2", mode))
        self.K5L1_2_select =bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_2_select", mode))
        self.K5L1_3_connection =bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_3_connection ", mode))
        self.K5L1_3= float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_3", mode))
        self.K5L1_3_select =bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_3_select", mode))
        self.K5L1_4_connection =bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_4_connection", mode))
        self.K5L1_4 =float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_4", mode))
        self.K5L1_4_select =bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L1_4_select", mode))
        self.K5P5_1 =float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P5_1", mode))
        self.K5P5_1_select =bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P5_1_select", mode))
        self.K5P5_2 =float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P5_2", mode))
        self.K5P5_2_select =bool(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P5_2_select", mode))
        self.purge_proved = False
        self.K5Q3 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5Q3", mode))
        self.K5T17 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T17", mode))
        self.K5V10 = False
        self.K5V7 = False
        self.K5V8 = False
        self.K5T3 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T3", mode))
        self.K5V9 = False
        self.K5T14 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T14", mode))
        self.K5V3 = False
        self.K5T6 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T6", mode))
        self.K5P10 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P10", mode))
        self.K5T15 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T15", mode))
        self.K5T16 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T16", mode))
        self.K5P8 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P8", mode))
        self.K5T2_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T2_1", mode))
        self.K5T2_1_select = True
        self.K5T2_2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T2_2", mode))
        self.K5T2_2_select = False
        self.K5V12 = False
        self.K5F11 = False
        self.K5F5 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5F5", mode))
        self.K5L2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5L2", mode))
        self.K5P13 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P13", mode))
        self.K5P13_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P13", mode))
        self.K5LCV1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5LCV1", mode))
        self.K5LCV2=float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5LCV2", mode))
        self.K5LCV1_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5LCV1_1", mode))
        self.K5F6x = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5F6x", mode))
        self.K0P102_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K0P102_1", mode))
        self.K5TCV2=float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5TCV2", mode))
        self.K0T104_2 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K0T104_2", mode))
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
        self.K5Q2_1 = 0
        self.K5Q2_2 = 0
        self.K5P4_1 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P4_1", mode))
        self.K5P4_1_select = True
        self.K5P4_2 = self.K5P4_1
        self.K5P4_2_select = True
        K5V28 = False
        K5HCV53 = False
        self.K5F3 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5F3", mode))
        self.K5T20 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5T20", mode))
        self.K5P110 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5P110", mode))
        self.K5PCV4 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV4", mode))
        K5P23 = 0
        K5P24 = 0
        self.K5Q3 = 0
        self.K5P6_1 = 0
        K5P6_1_select = True
        self.K5P6_2 = 0
        K5P6_2_select = False
        self.K0P125 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV4", mode))
        K5HCV27_1 = True
        K5HCV26_1 = True
        K5HCV27_2 = True
        K5HCV26_2 = True
        K5HCV50_1 = False
        K5V51_1 = False
        self.K5PCV17_1 = 0
        K5PCV17_1_task = 0
        self.K5P17_1 = 0
        K5HCV50_2 = False
        K5V51_2 = False
        K5PCV17_2 = 0
        K5PCV17_2_task = 0
        self.K5P17_2 = 0
        K5HCV50 = False
        K5HCV51 = False
        igniter_1 = False
        igniter_2 = False
        burner_1 = False
        burner_2 = False
        self.K5P16_1 = 0
        self.K5P16_2 = 0
        K5HCV60 = 0
        K5HCV60_task = 0
        K5HCV61 = 0
        K5HCV61_task = 0
        self.K5T12 = 0
        self.K5PCV6CHOP = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV6CHOP", mode))
        self.K5PC5CHOP = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PC5CHOP", mode))
        self.K5BSB_2=float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5BSB_2", mode))
        # self.Ksmoke_pump = Smoke_pump(mode)
        # self.KK5PCV5 = K5PCV5(mode)
        # self.KK5HCV62 = K5HCV62(mode)
        # self.KK5HCV63 = K5HCV63(mode)
        # self.fun=Fan(mode)
        self.KK5TCV2=K5TCV2_control(self.K5TCV2)
        self.KK5LCV1 = K5LCV1_control(self.K5LCV1)
        self.KK5PCV4 = K5PCV4_control(self.K5PCV4)
        self.KK5LCV1_1 = K5lCV1_1_control(self.K5LCV1_1)
        self.K5F6x_excitement=0
        self.K5F5_excitement=0
        self.K5F3_excitement=0
        self.K5L1_1_excitement=0
        self.K5T15_excitement=0
        self.K5T16_excitement = 0
        self.K5T17_excitement = 0
        self.K5P10_excitement = 0
        self.K5T6_excitement=0
        self.K5P8_excitement = 0
        self.K5L2_excitement=0
        self.K5T14_excitement = 0
        self.K0T104_2_excitement = 0
        self.K0P102_1_excitement = 0
        self.K5P13_excitement=0
        self.K5P13_1_excitement=0
        self.K5P5_1_excitement=0
        self.K5P5_2_excitement=0
        self.K5Q3_excitement=0
        self.K5L1_2_excitement=0
        self.K5L1_3_excitement=0
        self.K5L1_4_excitement=0
        self.K0P125_excitement=0
        self.K5T20_excitement = 0
        self.K5P110_excitement = 0
        self.K5P4_1_excitement = 0

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
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T9_2.sav'), 'rb'))
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
        entrance = {'K5P10.PV': [self.K5P10]}
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
        entrance = {'K5F6X.PV': [self.K5F6x]}
        table_entrance = pd.DataFrame(data=entrance)
        out=(float(model.predict(table_entrance)[0][0]))
        return out

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
        entrance = {'K5F5.PV': [self.K5F5], 'K5F6X.PV': [self.K5F6x], }
        table_entrance = pd.DataFrame(data=entrance)
        self.K5L1_2 = float(model.predict(table_entrance)[0][0])+self.K5L1_2_excitement

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
        entrance = {'K5F5.PV': [self.K5F5], 'K5F6X.PV': [self.K5F6x], }
        table_entrance = pd.DataFrame(data=entrance)
        self.K5L1_3 = float(model.predict(table_entrance)[0][0])+self.K5L1_3_excitement

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
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5L1_3.sav'), 'rb'))
        entrance = {'K5F5.PV': [self.K5F5], 'K5F6X.PV': [self.K5F6x]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5L1_4 = float(model.predict(table_entrance)[0][0])+self.K5L1_4_excitement

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

    def change_K5Q3(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5Q3.sav'), 'rb'))
        entrance = {'K5BSB_2.PV': [self.K5BSB_2]}
        cube = PolynomialFeatures(degree=3)
        table_entrance = pd.DataFrame(data=entrance)
        self.K5Q3 = float(model.predict(cube.fit_transform(table_entrance))[0][0])+self.K5Q3_excitement

    # TODO:Переобучит сеть в K5Q3

    def change_K5T15(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T15.sav'), 'rb'))
        entrance = {'K5F5.PV':[self.K5F5],'K5F6X.PV':[self.K5F6x],'K5T16.PV':[self.K5T16],'K5T17.PV':[self.K5T17]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T15= float(model.predict(table_entrance)[0][0])+self.K5T15_excitement

    def change_K5T3(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T3.sav'), 'rb'))
        entrance = {'K5TCV2I.PV':[self.K5TCV2]}
        cube = PolynomialFeatures(degree=3)
        table_entrance = pd.DataFrame(data=entrance)
        F3= float(model.predict(cube.fit_transform(table_entrance))[0][0])
        H_steam=2800+2.5*(self.K5T14-250)
        def cp_water(T):
            cp = 4.18
            return cp
        T_start = 298
        T_end = self.K5T15 + 273
        integral_result, error = spi.quad(cp_water, T_start, T_end)
        H_298 = 108.53  # Заполните соответствующее значение начальной энтальпии при 298 K
        H_water = H_298 + integral_result
        H_out=(H_steam*(self.K5F6x*0.278)-H_water*((F3-4)*0.278))/(self.K5F6x*0.278)
        self.K5T3=(((H_out-2800)/4.18+250+273)-273)

    def change_K5T14(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T14.sav'), 'rb'))
        entrance = {'K5PS14_1.PV':[self.K5PS14_1],'K5PS14_2.PV':[self.K5PS14_2],'K5F6X.PV':[self.K5F6x]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T14= float(model.predict(table_entrance)[0][0])+self.K5T14_excitement

    def change_K5T6(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T6.sav'), 'rb'))
        entrance = {'K5F5.PV': [self.K5F5],"K5F6X.PV":[self.K5F6x], "K5T17.PV":[self.K5T17]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T6= float(model.predict(table_entrance)[0][0])+self.K5T6_excitement

    def change_K5P10(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P10.sav'), 'rb'))
        entrance = {'K5PS14_2.PV':[self.K5PS14_2]}
        quadratic = PolynomialFeatures(degree=2)
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P10= float(model.predict(quadratic.fit_transform(table_entrance))[0][0])+self.K5P10_excitement

    def change_K5T16(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T16.sav'), 'rb'))
        entrance = {'K0P102_1.PV':[self.K0P102_1]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T16= float(model.predict(table_entrance)[0][0])+self.K5T16_excitement

    def change_K5T17(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T17.sav'), 'rb'))
        entrance = {'K5PS14_2.PV':[self.K5PS14_2], 'K5T6.PV':[self.K5T6], 'K5P10.PV':[self.K5P10], 'K5LCV1I.PV':[self.K5LCV1],
                    'K5F5.PV':[self.K5F5],'K5T14.PV':[self.K5T14],'K5TCV2I.PV':[self.K5LCV2], 'K5F6X.PV':[self.K5F6x],
                    'K5T15.PV':[self.K5T15],'K5P8.PV':[self.K5P8]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T17= float(model.predict(table_entrance)[0][0])+self.K5T17_excitement

    def change_K5P8(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P8.sav'), 'rb'))
        entrance = {'K5PS14_1.PV':[self.K5PS14_1]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P8= float(model.predict(table_entrance)[0][0])+self.K5P8_excitement

    def change_K5T2_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T2_1.sav'), 'rb'))
        entrance = {'K5T3.PV':[self.K5T3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T2_1= float(model.predict(table_entrance)[0][0])

    def change_K5T2_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T2_2.sav'), 'rb'))
        entrance = {'K5T3.PV':[self.K5T3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5T2_2= float(model.predict(table_entrance)[0][0])

    def change_K5F5(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5F5.sav'), 'rb'))
        entrance = {'K5LCV1I.PV':[self.K5LCV1+self.K5LCV1_1]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5F5= float(model.predict(table_entrance)[0][0])+self.K5F5_excitement

    def change_K5F3(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5F3.sav'), 'rb'))
        entrance = {'K5PCV4I.PV':[self.K5PCV4]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5F3= float(model.predict(table_entrance)[0][0])+self.K5F3_excitement

    def change_K5L2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5L2.sav'), 'rb'))
        entrance = {'K5T3.PV':[self.K5T3], 'K5TCV2I.PV':[self.K5TCV2]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5L2= float(model.predict(table_entrance)[0][0])+self.K5L2_excitement

    def change_K5F6x(self):
        self.K5F6x=self.K5F3/100+self.K5F6x_excitement

    def K5LCV1_autotask(self, K5F5):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5LCV1_auto.sav'), 'rb'))
        entrance = {'K5F5.PV': [K5F5]}
        table_entrance = pd.DataFrame(data=entrance)
        quadratic = PolynomialFeatures(degree=2)
        out=(float(model.predict(quadratic.fit_transform(table_entrance))[0][0]))
        return out

    def change_K0P102_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K0P102_1.sav'), 'rb'))
        entrance = {'K5PS14_1.PV':[self.K5PS14_1]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K0P102_1= float(model.predict(table_entrance)[0][0])+self.K0P102_1_excitement

    def change_K0T104_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K0T104_2.sav'), 'rb'))
        entrance = {'K5T2_1.PV':[self.K5T2_1]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K0T104_2= float(model.predict(table_entrance)[0][0])+self.K0T104_2_excitement

    def change_K5P13(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P13.sav'), 'rb'))
        entrance = {'K5P6.PV':[self.K5P6_1],'K5P17_1.PV':[self.K5P17_1], 'K5P17_2.PV':[self.K5P17_1], 'K5F3.PV':[self.K5F3],
                    'K5PCV4I.PV':[self.K5PCV4], 'K5T12.PV':[self.K5T12] ,
             'K5P16_1.PV':[self.K5P16_1], 'K5P16_2.PV':[self.K5P16_2], 'K5Q2_1.PV':[self.K5Q2_1], 'K5P4_1.PV':[self.K5P4_1]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P13= float(model.predict(table_entrance)[0][0])+self.K5P13_excitement

    def change_K5P13_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P13.sav'), 'rb'))
        entrance = {'K5P6.PV':[self.K5P6_1],'K5P17_1.PV':[self.K5P17_1], 'K5P17_2.PV':[self.K5P17_1], 'K5F3.PV':[self.K5F3],
                    'K5PCV4I.PV':[self.K5PCV4], 'K5T12.PV':[self.K5T12] ,
             'K5P16_1.PV':[self.K5P16_1], 'K5P16_2.PV':[self.K5P16_2], 'K5Q2_1.PV':[self.K5Q2_1], 'K5P4_1.PV':[self.K5P4_1]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P13_1= float(model.predict(table_entrance)[0][0])+self.K5P13_1_excitement+0.5

    def change_K5P5_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P5_1.sav'), 'rb'))
        entrance = {'K5PC5CH.OP':[self.K5PC5CHOP], 'K5PC6CH.OP':[self.K5PCV6CHOP], 'K5F3.PV':[self.K5F3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P5_1= float(model.predict(table_entrance)[0][0])+self.K5P5_1_excitement

    def change_K5P5_2(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P5_2.sav'), 'rb'))
        entrance = {'K5PC5CH.OP':[self.K5PC5CHOP], 'K5PC6CH.OP':[self.K5PCV6CHOP], 'K5F3.PV':[self.K5F3]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P5_2= float(model.predict(table_entrance)[0][0])+self.K5P5_2_excitement

    def change_K0P125(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K0P125.sav'), 'rb'))
        entrance = {'K5P110.PV':[self.K5P110]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K0P125= float(model.predict(table_entrance)[0][0])+self.K0P125_excitement

    def change_K5T20(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5T20.sav'), 'rb'))
        entrance = {'K5PCV17_1I.PV':[self.K5PCV17_1]}
        table_entrance = pd.DataFrame(data=entrance)
        quadratic = PolynomialFeatures(degree=2)
        self.K5T20= float(model.predict(quadratic.fit_transform(table_entrance))[0][0])+self.K5T20_excitement

    def change_K5P110(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P110.sav'), 'rb'))
        entrance = {'K0P125.PV':[self.K0P125]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P110= float(model.predict(table_entrance)[0][0])+self.K5P110_excitement

    def change_K5P4_1(self):
        model = pickle.load(open(Path(Path.cwd(), 'models', "model", 'K5P4_1.sav'), 'rb'))
        entrance = {'K0P125.PV':[self.K0P125], 'K5PCV4I.PV': [self.K5PCV4]}
        table_entrance = pd.DataFrame(data=entrance)
        self.K5P4_1= float(model.predict(table_entrance)[0][0])+self.K5P4_1_excitement




class Smoke_pump():
    def __init__(self, mode):
        self.smoke_pump = Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "smoke_pump", mode)
        self.current_smoke_pump = int(
            Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "current_smoke_pump", mode))
        self.K5PC5CHSP = int(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PC5CHSP", mode))
        self.K5PC5CHOP = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PC5CHOP", mode))
        self.K5PC5CHMO = Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PC5CHMO", mode)
        self.K5PC5CHOP_task = float(
            Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PC5CHOP", mode))
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
            Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV5_task", mode))
        self.K5PCV5 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV5", mode))
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
            Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5HCV63_task", mode))
        self.K5HCV63 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV5", mode))
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
            Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5HCV62_task", mode))
        self.K5HCV62 = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV5", mode))
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
        self.fun = Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "fun", mode)
        self.current_fun = int(
            Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "current_fun", mode))
        self.K5PCV6CHSP = int(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV6CHSP", mode))
        self.K5PCV6CHOP = float(Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV6CHOP", mode))
        self.K5PCV6CHMO = Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV6CHMO", mode)
        self.K5PCV6CHOP_task = float(
            Scripts.Tab(Path(Path.cwd(), 'database', 'mode.csv'), "объект", "K5PCV65CHOP", mode))
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

class K5TCV2_control():
    def __init__(self, K5TCV2):
        self.K5TCV2_task = K5TCV2
        self.K5TCV2 = K5TCV2
        self.speed = 1.11

    def adjustment(self, K5TCV2_task=-101):
        if K5TCV2_task!=-101:
            self.K5TCV2_task=K5TCV2_task

        if self.K5TCV2_task > self.K5TCV2:
            self.open()
        elif self.K5TCV2_task < self.K5TCV2:
            self.close()
        return self.K5TCV2

    def open(self):
        if self.K5TCV2 + self.speed >= self.K5TCV2_task:
            if self.K5TCV2_task<100:
                self.K5TCV2 = self.K5TCV2_task
            else:
                self.K5TCV2=100
        else:
            if self.K5TCV2 +self.speed<100:
                self.K5TCV2 += self.speed
            else:
                self.K5TCV2=100

    def close(self):
        if self.K5TCV2 - self.speed <= self.K5TCV2_task:
            if self.K5TCV2_task>0:
                self.K5TCV2 = self.K5TCV2_task
            else:
                self.K5TCV2=0
        else:
            if self.K5TCV2 - self.speed>0:
                self.K5TCV2 -= self.speed
            else:
                self.K5TCV2=0

class K5lCV1_1_control():
    def __init__(self, K5LCV1_1):
        self.K5LCV1_1_task = K5LCV1_1
        self.K5LCV1_1 = K5LCV1_1
        self.speed = 1.11

    def adjustment(self, K5LCV1_1_task=-101, level=0):
        if K5LCV1_1_task != -101:
            self.K5LCV1_1_task = K5LCV1_1_task
        elif level != 0:
            adjustment = level * 0.5
            self.K5LCV1_1_task = self.K5LCV1_task + adjustment
        if self.K5LCV1_1_task > self.K5LCV1_1:
            self.open()
        elif self.K5LCV1_1_task < self.K5LCV1_1:
            self.close()
        return self.K5LCV1_1

    def open(self):
        if self.K5LCV1_1 + self.speed >= self.K5LCV1_1_task:
            if self.K5LCV1_1_task<100:
                self.K5LCV1_1 = self.K5LCV1_1_task
            else:
                self.K5LCV1_1=100
        else:
            if self.K5LCV1_1 + self.speed<100:
                self.K5LCV1_1 += self.speed
            else:
                self.K5LCV1_1=100

    def close(self):
        if self.K5LCV1_1 - self.speed <= self.K5LCV1_1_task:
            if self.K5LCV1_1_task>0:
                self.K5LCV1_1 = self.K5LCV1_1_task
            else:
                self.K5LCV1_1=0
        else:
            if self.K5LCV1_1 - self.speed>0:
                self.K5LCV1_1 -= self.speed
            else:
                self.K5LCV1_1=0

class K5LCV1_control():
    def __init__(self, K5LCV1):
        self.K5LCV1_task = K5LCV1
        self.K5LCV1 = K5LCV1
        self.speed = 1.11

    def adjustment(self, K5LCV1_task = -101, level=0):
        if K5LCV1_task!= -101:
            self.K5LCV1_task = K5LCV1_task
        elif level!=0:
            adjustment=level*0.5
            self.K5LCV1_task=self.K5LCV1_task+adjustment
        if self.K5LCV1_task > self.K5LCV1:
            self.open()
        elif self.K5LCV1_task < self.K5LCV1:
            self.close()
        return self.K5LCV1

    def regulate_pin(self, current_position, level):
        factory = PiGPIOFactory()
        pin = PWMOutputDevice(18, pin_factory=factory)
        pin.value = current_position
        while True:
            if level > 350:
                level = 350
            elif level < -350:
                level = -350
            duty_cycle = level / 700
            pin.value = duty_cycle
            print(pin.value)
        return pin.value


    def open(self):
        if self.K5LCV1 + self.speed >= self.K5LCV1_task:
            if self.K5LCV1_task<100:
                self.K5LCV1 = self.K5LCV1_task
            else:
                self.K5LCV1=100
        else:
            if self.K5LCV1 + self.speed<100:
                self.K5LCV1 += self.speed
            else:
                self.K5LCV1=100

    def close(self):
        if self.K5LCV1 - self.speed <= self.K5LCV1_task:
            if self.K5LCV1_task>0:
                self.K5LCV1 = self.K5LCV1_task
            else:
                self.K5LCV1=0
        else:
            if self.K5LCV1 - self.speed>0:
                self.K5LCV1 -= self.speed
            else:self.K5LCV1=0

class K5PCV4_control():
    def __init__(self, K5PCV4):
        self.K5PCV4_task = K5PCV4
        self.K5PCV4 = K5PCV4
        self.speed = 1.11

    def adjustment(self, K5PCV4_task = -1):
        if K5PCV4_task!= -1:
            self.K5PCV4_task = K5PCV4_task  # пробросить число от пользователя
        if self.K5PCV4_task > self.K5PCV4:
            self.open()
        elif self.K5PCV4_task < self.K5PCV4:
            self.close()
        return self.K5PCV4

    def open(self):
        if self.K5PCV4 + self.speed >= self.K5PCV4_task:
            if self.K5PCV4_task < 100:
                self.K5PCV4 = self.K5PCV4_task
            else:
                self.K5PCV4=100
        else:
            if self.K5PCV4 + self.speed<100:
                self.K5PCV4 += self.speed
            else:
                self.K5PCV4 = 100

    def close(self):
        if self.K5PCV4 - self.speed <= self.K5PCV4_task:
            if self.K5PCV4_task>0:
                self.K5PCV4 = self.K5PCV4_task
            else:
                self.K5PCV4=0
        else:
            if self.K5PCV4 - self.speed>0:
                self.K5PCV4 -= self.speed
            else:
                self.K5PCV4