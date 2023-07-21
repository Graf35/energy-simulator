#Эти библиотеки позволяют работать с графикой.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import  uic
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import os
from equipment.steam_boiler_E5039440gm5 import Steam_boiler
from PyQt5.QtWidgets import QApplication, QMainWindow
import asyncio
from time import sleep
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import MultiTaskLassoCV
from sklearn.linear_model import Ridge
import seaborn as sns
from scipy.stats import norm
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score

#Определяем имяи путь до файлас формой окна.
ui=uic.loadUiType("interface/testing_window.ui")[0]

#Этот класс определяет параметры окна и взаимодействие с ним.
class Testing_window(QtWidgets.QMainWindow, ui):
    def __init__(self, mode):
        super().__init__()
        self.setupUi(self)
        self.management_button.clicked.connect(self.management_1)
        self.excitement_botton.clicked.connect(self.excitement)
        self.bolier = Steam_boiler(mode)
        self.work_deman = threading.Thread(target=self.work, daemon=True)
        self.work_deman.start()
        self.updater_deman = threading.Thread(target=self.updater, daemon=True)
        self.updater_deman.start()
        self.power_supply_node()

    def steam_cooler(self):
        self.Legend_1.setText("text2")

    def power_supply_node(self):
        self.Legend_1.setText("Расход пара")
        self.value_1.setText(str(self.bolier.K5F6x))
        self.unit_1.setText("Т/Ч")
        self.Legend_2.setText("уровень в барабане")
        self.value_2.setText(str(self.bolier.K5L1_1))
        self.unit_2.setText("мм")
        self.Legend_3.setText("Расход питательной воды")
        self.value_3.setText(str(self.bolier.K5F5))
        self.unit_3.setText("Т/Ч")
        self.Legend_4.setText("Положение клапана по питательной воде")
        self.value_4.setText(str(self.bolier.K5LCV1))
        self.unit_4.setText("%")
        self.Legend_5.setText("Расход газа на котёл")
        self.value_5.setText(str(self.bolier.K5F3))
        self.unit_5.setText("л")
        self.Legend_6.setText("Положение клапана по газу")
        self.value_6.setText(str(self.bolier.K5PCV4))
        self.unit_6.setText("%")
        self.management_params_1.addItem("K5LCV1")
        self.management_params_2.addItem("K5PCV4")
        self.excitement_params.addItems(["K5L1_1", "K5F6x", "K5F3", "K5F5"])

    def management_1(self):
        task = self.management_task_1.toPlainText()
        self.management_task_1.clear()
        if task!="":
            self.bolier.K5LCV1=self.bolier.KK5LCV1.adjustment(float(task))
        self.management_2()
    def management_2(self):
        task = self.management_task_2.toPlainText()
        self.management_task_2.clear()
        if task!="":
            self.bolier.K5PCV4=self.bolier.KK5PCV4.adjustment(float(task))

    def updater(self):
        self.value_1.setText(str(self.bolier.K5F6x))
        self.value_2.setText(str(self.bolier.K5L1_1))
        self.value_3.setText(str(self.bolier.K5F5))
        self.value_4.setText(str(self.bolier.K5LCV1))
        self.value_5.setText(str(self.bolier.K5F3))
        self.value_6.setText(str(self.bolier.K5PCV4))

    def drum_lavel(self):
        K5F5=self.bolier.change_K5L1_1()
        self.bolier.K5L1_1+=(((self.bolier.K5F5-K5F5)))+self.bolier.K5L1_1_excitement
        self.bolier.K5LCV1 = self.bolier.KK5LCV1.adjustment(K5LCV1_task=(self.bolier.K5LCV1_autotask(K5F5)))





    def work(self):
        while True:
            self.bolier.K5LCV1 = self.bolier.KK5LCV1.adjustment()
            self.bolier.change_K5F5()
            self.drum_lavel()
            self.bolier.K5PCV4=self.bolier.KK5PCV4.adjustment()
            self.bolier.change_K5F3()
            self.bolier.change_K5F6x()
            self.updater()
            sleep(2)

    def excitement(self):
        task = float(self.excitement_task.toPlainText())
        parametr = self.excitement_params.currentText()
        self.excitement_task.clear()
        setattr(self.bolier, parametr+"_excitement", task)
