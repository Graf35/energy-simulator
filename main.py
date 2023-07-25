# Импортируем модуль Window. Он необходим для создания графического окна
import main_window
#Импортируем PyQt5 для работы с графикой
from PyQt5 import QtWidgets
#Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.
import sys
import os
import pika
import webbrowser


def main():
    # Подключение к серверу RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    try:
        # Отправка тестового сообщения на очередь
        channel.queue_declare(queue='test')
        channel.basic_publish(exchange='', routing_key='test', body='Test message')
        webbrowser.open('http://localhost:15672')
        print("Сервер RabbitMQ работает и доступен")
    except pika.exceptions.AMQPConnectionError:
        os.chdir("C:\\Program Files\\RabbitMQ Server\\rabbitmq_server-3.12.2\\sbin")
        os.system('rabbitmq-server start')
        webbrowser.open('http://localhost:15672')
        print("Сервер RabbitMQ запущен")
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = main_window.MaimWindow()  # Создаём объект класса
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()