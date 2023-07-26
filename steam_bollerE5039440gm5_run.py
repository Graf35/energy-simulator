#Эти библиотеки позволяют работать с графикой.

from PyQt5 import QtWidgets

from PyQt5 import  uic
import threading
import pika
from equipment.steam_boiler_E5039440gm5 import Steam_boiler
from time import sleep



#Этот класс определяет параметры окна и взаимодействие с ним.
class Steam_bollerE5039440gm5():
    def __init__(self, mode):
        super().__init__()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.connection2 = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel2= self.connection.channel()
        self.channel2.queue_declare(queue='boiler_data')
        self.listening_deman = threading.Thread(target=self.listening_queue, daemon=True)
        self.listening_deman.start()
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
        # self.bolier.K5LCV1 = self.bolier.KK5LCV1.adjustment(K5LCV1_task=(self.bolier.K5LCV1_autotask(K5F5)))





    def work(self):
        while True:
            self.bolier.K5LCV1 = self.bolier.KK5LCV1.adjustment()
            self.bolier.change_K5F5()
            self.send_data("K5LCV1 "+str(self.bolier.K5LCV1))
            self.send_data("K5F5 "+str(self.bolier.K5F5))
            self.drum_lavel()
            self.bolier.K5PCV4=self.bolier.KK5PCV4.adjustment()
            self.bolier.change_K5F3()
            self.bolier.change_K5F6x()
            self.bolier.change_K5T15()
            self.bolier.change_K5T16()
            self.bolier.change_K5T17()
            self.bolier.change_K5P10()
            sleep(2)

    def excitement(self):
        task = float(self.excitement_task.toPlainText())
        parametr = self.excitement_params.currentText()
        self.excitement_task.clear()
        setattr(self.bolier, parametr+"_excitement", task)

    def run_boler(self):
        self.bolier.K5LCV1 = self.bolier.KK5LCV1.adjustment()
        self.bolier.change_K5F5()
        self.drum_lavel()
        self.bolier.K5PCV4 = self.bolier.KK5PCV4.adjustment()
        self.bolier.change_K5F3()
        self.bolier.change_K5F6x()
        self.bolier.change_K5T15()
        self.bolier.change_K5T16()
        self.bolier.change_K5T17()

    def send_data(self, data):
        # Отправка данных в RabbitMQ
        self.channel.basic_publish(exchange='', routing_key='data_queue', body=str(data))

    def process_data(self, data):
        variable, value = data.split()
        tag_to_func = {"K5LCV1":self.bolier.KK5LCV1.adjustment(float(value))}
        tag_to_func[variable]


    # Callback-функция для обработки полученных сообщений
    def callback(self, ch, method, properties, body):
        self.process_data(body.decode())

    def listening_queue(self):
        self.channel2.basic_consume(queue='boiler_data', on_message_callback=self.callback, auto_ack=True)
        self.channel2.start_consuming()
    def __del__(self):
        # Закрытие соединения с RabbitMQ
        self.connection.close()
        self.connection2.close()