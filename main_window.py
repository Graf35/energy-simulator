#Эти библиотеки позволяют работать с графикой.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import  uic
import threading
import steam_bollerE5039440gm5_run
import sys
import asyncio

#Определяем имяи путь до файлас формой окна.
ui=uic.loadUiType("interface/main_window.ui")[0]

#Этот класс определяет параметры окна и взаимодействие с ним.
class MaimWindow(QtWidgets.QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClicked)

        # Этот метод описывает действи при нажатии кнопки

    def btnClicked(self):
        try:
            self.test= steam_bollerE5039440gm5_run.Testing_window(self.comboBox_2.currentText())
            asyncio.run(self.show_window())
        except:
            pass


    async def show_window(self):
        self.test.show()






