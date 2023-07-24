#Эти библиотеки позволяют работать с графикой.
import queue

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import  uic
import threading
import multiprocessing
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import os
import subprocess

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
        # subprocess.call(['python', 'steam_and_water.py', self])
        # s=steam_and_water.Steam_and_water(self)


    def steam_cooler(self):
        self.Legend_1.setText("text2")

    def power_supply_node(self):
        self.Legend_1.setText("Температура питательной воды до конденсатора")
        self.value_1.setText(str(self.bolier.K5T16))
        self.unit_1.setText("C")
        self.Legend_2.setText("Температура питательной воды после конденсатора")
        self.value_2.setText(str(self.bolier.K5T17))
        self.unit_2.setText("C")
        self.Legend_3.setText("Температура конденсата")
        self.value_3.setText(str(self.bolier.K5T15))
        self.unit_3.setText("C")
        self.Legend_4.setText("Давление питательной воды")
        self.value_4.setText(str(self.bolier.K5P10))
        self.unit_4.setText("МПа")
        self.management_params_1.addItem("")
        self.management_params_2.addItem("")
        self.excitement_params.addItems(["K5T16", "K5T17", "K5T15"])


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
        self.value_1.setText(str(self.bolier.K5T16))
        self.value_2.setText(str(self.bolier.K5T17))
        self.value_3.setText(str(self.bolier.K5T15))
        self.value_4.setText(str(self.bolier.K5P10))
        self.value_5.setText(str(self.bolier.K5LCV1))
        # self.value_6.setText(str(self.bolier.K5PCV4))

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
            self.bolier.change_K5T15()
            self.bolier.change_K5T16()
            self.bolier.change_K5T17()
            self.bolier.change_K5P10()
            self.updater()
            # queue.put(self.bolier.K5F5)
            sleep(2)

    def excitement(self):
        task = float(self.excitement_task.toPlainText())
        parametr = self.excitement_params.currentText()
        self.excitement_task.clear()
        setattr(self.bolier, parametr+"_excitement", task)

    def run_boler(self):
        self.bolier.K5LCV1 = self.bolier.KK5LCV1.mechanic_adjustment()
        self.bolier.change_K5F5()
        self.drum_lavel()
        self.bolier.K5PCV4 = self.bolier.KK5PCV4.mechanic_adjustment()
        self.bolier.change_K5F3()
        self.bolier.change_K5F6x()
        self.bolier.change_K5T15()
        self.bolier.change_K5T16()
        self.bolier.change_K5T17()

    def start_process(self):
        my_queue = multiprocessing.Queue()
        p = multiprocessing.Process(target=self.work(my_queue))
        p.start()
        return my_queue