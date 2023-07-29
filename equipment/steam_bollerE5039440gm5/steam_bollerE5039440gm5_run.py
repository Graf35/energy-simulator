import asyncio
import threading
import pika
from equipment.steam_bollerE5039440gm5.steam_boiler_E5039440gm5 import Steam_boiler
from time import sleep
import Scripts
import os
import logging
from Log import Deman_log

class Steam_bollerE5039440gm5():
    def __init__(self, mode):
        super().__init__()
        logger = Deman_log()
        self.config = Scripts.filereader("config.config")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.config["rabbimq_main_server"]))
        self.channel = self.connection.channel()
        self.connection2 = pika.BlockingConnection(pika.ConnectionParameters(host=self.config["rabbimq_main_server"]))
        self.channel2= self.connection.channel()
        self.channel2.queue_declare(queue='boiler_data')
        self.listening_deman = threading.Thread(target=self.listening_queue, daemon=True)
        self.listening_deman.start()
        self.bolier = Steam_boiler(mode)
        self.run_deman = threading.Thread(target=self.run_boler, daemon=True)
        self.run_deman.start()



    def run_boler(self):
        while True:
            self.bolier.K5LCV1 = self.bolier.KK5LCV1.adjustment()
            self.send_data("K5LCV1 " + str(round(self.bolier.K5LCV1, 2)))
            self.bolier.K5LCV1_1=self.bolier.KK5LCV1_1.adjustment()
            self.send_data("K5LCV1_1 " + str(round(self.bolier.K5LCV1_1, 2)))
            self.bolier.change_K5F5()
            self.send_data("K5F5 "+str(round(self.bolier.K5F5,2)))
            self.bolier.change_K5T16()
            self.send_data("K5T16 " + str(round(self.bolier.K5T16, 2)))
            self.bolier.change_K5T17()
            self.send_data("K5T17 " + str(round(self.bolier.K5T17, 2)))
            self.bolier.change_K5P10()
            self.send_data("K5P10 " + str(round(self.bolier.K5P10, 2)))
            self.bolier.change_K5T6()
            self.send_data("K5T6 " + str(round(self.bolier.K5T6, 2)))
            self.bolier.change_K5T15()
            self.send_data("K5T15 " + str(round(self.bolier.K5T15, 2)))
            self.bolier.change_K5P8()
            self.send_data("K5P8 " + str(round(self.bolier.K5P8, 2)))
            self.bolier.change_K5L2()
            self.send_data("K5L2 " + str(round(self.bolier.K5L2, 2)))
            self.bolier.K5TCV2 = self.bolier.KK5TCV2.adjustment()
            self.send_data("K5TCV2 " + str(round(self.bolier.K5TCV2, 2)))
            self.bolier.change_K5T14()
            self.send_data("K5T14 " + str(round(self.bolier.K5T14, 2)))
            self.bolier.change_K5T3()
            self.send_data("K5T3 " + str(round(self.bolier.K5T3, 2)))
            self.bolier.change_K5T2_1()
            self.send_data("K5T2_1 " + str(round(self.bolier.K5T2_1, 2)))
            self.bolier.change_K5T2_2()
            self.send_data("K5T2_2 " + str(round(self.bolier.K5T2_2, 2)))
            self.bolier.change_K5T2_1()
            self.send_data("K5T2_1 " + str(round(self.bolier.K5T2_1, 2)))
            self.drum_lavel()
            self.bolier.K5PCV4=self.bolier.KK5PCV4.adjustment()
            self.bolier.change_K5F3()
            self.bolier.change_K5F6x()
            sleep(2)

    def drum_lavel(self):
        K5F5=self.bolier.change_K5L1_1()
        self.bolier.K5L1_1+=(((self.bolier.K5F5-K5F5)))+self.bolier.K5L1_1_excitement

    def send_data(self, data):
        self.channel.basic_publish(exchange='', routing_key='data_queue', body=str(data))

    def process_data(self, data):
        variable, value = data.split()
        if variable=="K5LCV1":
            self.bolier.KK5LCV1.adjustment(float(value))
        elif variable=="K5LCV1_1":
            self.bolier.KK5LCV1_1.adjustment(float(value))
        elif variable=="K5TCV2":
            self.bolier.KK5TCV2.adjustment(float(value))


    # Callback-функция для обработки полученных сообщений
    def callback(self, ch, method, properties, body):
        self.process_data(body.decode())

    def listening_queue(self):
        self.channel2.basic_consume(queue='boiler_data', on_message_callback=self.callback, auto_ack=True)
        self.channel2.start_consuming()

    async def screen_start(self):
        os.system('python equipment/steam_bollerE5039440gm5/screen/steam_and_water.py')
