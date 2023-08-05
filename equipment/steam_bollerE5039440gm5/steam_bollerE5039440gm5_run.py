import asyncio
import threading
from equipment.steam_bollerE5039440gm5.steam_boiler_E5039440gm5 import Steam_boiler
from time import sleep
import Scripts
import os
import logging
from Log import Deman_log
import socket

class Steam_bollerE5039440gm5():
    def __init__(self, mode):
        super().__init__()
        logger = Deman_log()
        self.config = Scripts.filereader("config.config")
        self.data=''
        # Создаем TCP-сокет и привязываем его к IP-адресу и порту сервера
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.config["main_server"], int(self.config["main_server_port"])))
        # Слушаем входящие соединения
        self.server_socket.listen()
        # Принимаем входящее соединение от клиента
        # self.client_socket, client_address = self.server_socket.accept()
        logging.info("Соединение установлено с клиентом: "+ str(self.client_address))
        self.bolier = Steam_boiler(mode)
        listening_deman = threading.Thread(target=self.anser_data, daemon=True)
        listening_deman.start()
        self.run_deman = threading.Thread(target=self.run_boler, daemon=True)
        self.run_deman.start()
        # self.screen_start()

    def run_boler(self):
        while True:
            self.client_socket, addr = self.server_socket.accept()
            logging.info(f"Accepted connection from {addr[0]}:{addr[1]}")
            client_thread = threading.Thread(target=self.handle_client, args=(self.client_socket,))
            client_thread.start()
            self.bolier.K5LCV1 = self.bolier.KK5LCV1.adjustment()
            self.data_append("K5LCV1 " + str(round(self.bolier.K5LCV1, 2)))
            self.bolier.K5LCV1_1=self.bolier.KK5LCV1_1.adjustment()
            self.data_append("K5LCV1_1 " + str(round(self.bolier.K5LCV1_1, 2)))
            self.bolier.change_K5F5()
            self.data_append("K5F5 "+str(round(self.bolier.K5F5,2)))
            self.bolier.change_K5T16()
            self.data_append("K5T16 " + str(round(self.bolier.K5T16, 2)))
            self.bolier.change_K5T17()
            self.data_append("K5T17 " + str(round(self.bolier.K5T17, 2)))
            self.bolier.change_K5P10()
            self.data_append("K5P10 " + str(round(self.bolier.K5P10, 2)))
            self.bolier.change_K5T6()
            self.data_append("K5T6 " + str(round(self.bolier.K5T6, 2)))
            self.bolier.change_K5T15()
            self.data_append("K5T15 " + str(round(self.bolier.K5T15, 2)))
            self.bolier.change_K5P8()
            self.data_append("K5P8 " + str(round(self.bolier.K5P8, 2)))
            self.bolier.change_K5L2()
            self.data_append("K5L2 " + str(round(self.bolier.K5L2, 2)))
            self.bolier.K5TCV2 = self.bolier.KK5TCV2.adjustment()
            self.data_append("K5TCV2 " + str(round(self.bolier.K5TCV2, 2)))
            self.bolier.change_K5T14()
            self.data_append("K5T14 " + str(round(self.bolier.K5T14, 2)))
            self.bolier.change_K5T3()
            self.data_append("K5T3 " + str(round(self.bolier.K5T3, 2)))
            self.bolier.change_K5T2_1()
            self.data_append("K5T2_1 " + str(round(self.bolier.K5T2_1, 2)))
            self.bolier.change_K5T2_2()
            self.data_append("K5T2_2 " + str(round(self.bolier.K5T2_2, 2)))
            self.bolier.change_K0P102_1()
            self.data_append("K0P102_1 " + str(round(self.bolier.K0P102_1, 2)))
            self.bolier.change_K0T104_2()
            self.data_append("K0T104_2 " + str(round(self.bolier.K0T104_2, 2)))
            self.bolier.change_K5F6x()
            self.data_append("K5F6x " + str(round(self.bolier.K5F6x, 2)))
            self.bolier.change_K5P13()
            self.data_append("K5P13 " + str(round(self.bolier.K5P13, 2)))
            self.bolier.change_K5P13_1()
            self.data_append("K5P13_1 " + str(round(self.bolier.K5P13_1, 2)))
            self.bolier.change_K5PS14_1()
            self.data_append("K5PS14_1 " + str(round(self.bolier.K5PS14_1, 2)))
            self.bolier.change_K5PS14_2()
            self.data_append("K5PS14_2 " + str(round(self.bolier.K5PS14_2, 2)))
            self.bolier.change_K5P5_2()
            self.data_append("K5P5_2 " + str(round(self.bolier.K5P5_2, 2)))
            self.bolier.change_K5P5_1()
            self.data_append("K5P5_1 " + str(round(self.bolier.K5P5_1, 2)))
            self.bolier.change_K5Q3()
            self.data_append("K5Q3 " + str(round(self.bolier.K5Q3, 2)))
            self.drum_lavel()
            self.data_append("K5L1_1 " + str(round(self.bolier.K5L1_1, 2)))
            self.data_append("K5L1_2 " + str(round(self.bolier.K5L1_2, 2)))
            self.data_append("K5L1_3 " + str(round(self.bolier.K5L1_3, 2)))
            self.data_append("K5L1_4 " + str(round(self.bolier.K5L1_4, 2)))
            self.bolier.K5PCV4=self.bolier.KK5PCV4.adjustment()
            self.bolier.change_K5F3()
            self.bolier.change_K5F6x()
            self.send_data()
            sleep(2)

    def drum_lavel(self):
        K5F5=self.bolier.change_K5L1_1()
        self.bolier.K5L1_1+=((0.0125*(self.bolier.K5F5-K5F5)**3))+self.bolier.K5L1_1_excitement
        self.bolier.K5L1_2 += ((0.125 * (self.bolier.K5F5 - K5F5) ** 3)) + self.bolier.K5L1_2_excitement
        self.bolier.K5L1_3 += ((0.125 * (self.bolier.K5F5 - K5F5) ** 3)) + self.bolier.K5L1_3_excitement
        self.bolier.K5L1_4 += ((0.125 * (self.bolier.K5F5 - K5F5) ** 3)) + self.bolier.K5L1_4_excitement

    def data_append(self, data):
        self.data+=data+"/n"

    def send_data(self):
        self.client_socket.send(self.data.encode())
        self.data=''

    def anser_data(self):
        while True:
            # Получаем данные от клиента
            data = self.client_socket.recv(1024).decode()
            if not data:
                break
            variable, value = data.split()
            print(variable)
            if variable=="K5LCV1":
                self.bolier.KK5LCV1.adjustment(float(value))
            elif variable=="K5LCV1_1":
                self.bolier.KK5LCV1_1.adjustment(float(value))
            elif variable=="K5TCV2":
                self.bolier.KK5TCV2.adjustment(float(value))

    def handle_client(self, client_socket):
        # обработка входящего соединения
        request = self.client_socket.recv(1024)
        logging.info(f"Received: {request}")
        self.client_socket.send(b"ACK")
        self.client_socket.close()

    async def screen_start(self):
        os.system('python equipment/steam_bollerE5039440gm5/screen/steam_and_water.py')
