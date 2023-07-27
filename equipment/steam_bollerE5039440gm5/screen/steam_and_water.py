from flask import Flask, jsonify, render_template, request
import webbrowser
import pika
import threading
import Scripts
import logging
from Log import Deman_log

logger = Deman_log()
config = Scripts.filereader("config.config")
connection = pika.BlockingConnection(pika.ConnectionParameters(host=config["rabbimq_main_screen"]))
channel = connection.channel()
channel.queue_declare(queue='data_queue')

K5F5 = 0
K5T16 = 0
K5LCV1 = 0
K5LCV1_1 = 0

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    #TODO Оператор Выбора
    if request.method == 'POST':
        K5LCV1_ans = request.form.get('K5LCV1_ans')
        if str(K5LCV1_ans) != "None":
            send_data("K5LCV1 " + str(K5LCV1_ans))
        K5LCV1_1_ans = request.form.get('K5LCV1_1_ans')
        if str(K5LCV1_1_ans) != "None":
            send_data("K5LCV1_1 " + str(K5LCV1_1_ans))
    return render_template('steam_and_water.html')


@app.route('/K5LCV1')
def update_K5LCV1():
    text = str(K5LCV1)
    return jsonify(K5LCV1=text)


@app.route('/K5LCV1_1')
def update_K5LCV1_1():
    text = str(K5LCV1_1)
    return jsonify(K5LCV1_1=text)


@app.route('/K5F5')
def update_K5F5():
    text = str(K5F5)
    return jsonify(K5F5=text)


@app.route('/K5T16')
def update_K5T16():
    text = str(K5T16)
    return jsonify(K5T16=text)


def process_data(data):
    variable, value = data.split()
    globals()[variable] = value


# Callback-функция для обработки полученных сообщений
def callback(ch, method, properties, body):
    process_data(body.decode())


def listening_queue():
    channel.basic_consume(queue='data_queue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


def send_data(data):
    # Отправка данных в RabbitMQ
    channel.basic_publish(exchange='', routing_key='boiler_data', body=str(data))


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    # Привязка callback-функции к очереди сообщений
    listening_deman = threading.Thread(target=listening_queue, daemon=True)
    listening_deman.start()
    app.run()
