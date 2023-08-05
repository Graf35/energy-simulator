#Эти библиотеки позволяют работать с графикой.
from PyQt5 import QtWidgets
from PyQt5 import  uic
import Scripts
from equipment.steam_bollerE5039440gm5 import steam_bollerE5039440gm5_run
import asyncio
import setting
import threading
import logging
from Log import Deman_log

#Определяем имяи путь до файлас формой окна.
ui=uic.loadUiType("interface/main_window.ui")[0]

#Этот класс определяет параметры окна и взаимодействие с ним.
class MaimWindow(QtWidgets.QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        logger = Deman_log()
        self.start_button.clicked.connect(self.start_button_clicked)
        self.setting.triggered.connect(self.show_setting_window)
        self.setting_window=setting.Setting()
        self.config = Scripts.filereader("config.config")


    def start_button_clicked(self):
        try:
            if self.type_equipment.currentText() == 'E-50-440-3,9ГМ':
                if self.equipment_mode.currentText()=='':
                    logging.warning("Не выбран сценарий запуска оборудования")
                asyncio.run(self.start_steam_bollerE5039440gm5())
                logging.info("Запущено оборудование: котёл Е-50-3,9-440ГМ")
            else:
                logging.warning("Не выбран тип оборудования")
        except:
            logging.error("Ошибка запуска оборудования "+str(self.type_equipment.currentText()))

    async def start_steam_bollerE5039440gm5(self):
        self.window= steam_bollerE5039440gm5_run.Steam_bollerE5039440gm5(self.equipment_mode.currentText())

    def show_setting_window(self):
        self.deman = threading.Thread(target=self.setting_window.show())
        self.deman.start()

