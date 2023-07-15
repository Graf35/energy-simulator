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

#Определяем имяи путь до файлас формой окна.
ui=uic.loadUiType("interface/testing_window.ui")[0]

#Этот класс определяет параметры окна и взаимодействие с ним.
class Testing_window(QtWidgets.QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.management_button.clicked.connect(self.management)
        self.bolier = Steam_boiler('Работа 20Т')
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
        self.management_params_1.addItem("K5LCV1")
        self.management_params_2.addItem("K5LCV1")
        self.excitement_params.addItems(["K5LCV1", "K5F6x", "K5L1_1", "K5F5"])

    def management(self):
        parametr = self.management_params_1.currentText()
        task = self.management_task_1.toPlainText()
        self.management_task_1.clear()
        setattr(self.bolier, parametr, task)

    def updater(self):
        self.value_1.setText(str(self.bolier.K5F6x))
        self.value_2.setText(str(self.bolier.K5L1_1))
        self.value_3.setText(str(self.bolier.K5F5))
        self.value_4.setText(str(self.bolier.K5LCV1))


    def work(self):
        while True:
            self.bolier.change_K5F5()
            self.updater()
            sleep(2)

