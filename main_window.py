#Эти библиотеки позволяют работать с графикой.
from PyQt5 import QtWidgets
from PyQt5 import  uic
import Scripts
import steam_bollerE5039440gm5_run
import asyncio
import os
import pika
import webbrowser
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
        self.rabbitmq_starter()


    def start_button_clicked(self):
        try:
            if self.type_equipment.currentText() == 'E-50-440-3,9ГМ':
                if self.equipment_mode.currentText()!='':
                    self.window= steam_bollerE5039440gm5_run.Steam_bollerE5039440gm5(self.equipment_mode.currentText())
                else:
                    logging.warning("Не выбран сценарий запуска оборудования")
            else:
                logging.warning("Не выбран тип оборудования")
            asyncio.run(self.show_window())
            logging.info("Запущено оборудование: котёл Е-50-3,9-440ГМ")
        except:
            logging.error("Ошибка запуска оборудования "+str(self.type_equipment.currentText()))

    async def show_window(self):
        self.window.show()

    def show_setting_window(self):
        self.deman = threading.Thread(target=self.setting_window.show())
        self.deman.start()

    def rabbitmq_starter(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.config["rabbimq_main_server"]))
        channel = connection.channel()
        try:
            # Отправка тестового сообщения на очередь
            channel.queue_declare(queue='test')
            channel.basic_publish(exchange='', routing_key='test', body='Test message')
            if self.config["developer_mode"]=="True":
                webbrowser.open('http://'+self.config["rabbimq_main_server"]+':15672')
            logging.info("Сервер RabbitMQ работает и доступен")
        except pika.exceptions.AMQPConnectionError:
            os.chdir("C:\\Program Files\\RabbitMQ Server\\rabbitmq_server-3.12.2\\sbin")
            os.system('rabbitmq-server start')
            if self.config["developer_mode"] == "True":
                webbrowser.open('http://'+self.config["rabbimq_main_server"]+':15672')
            logging.info("Сервер RabbitMQ запущен")
