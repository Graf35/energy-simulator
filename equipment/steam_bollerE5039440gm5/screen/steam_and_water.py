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
K5T17=0
K5T6=0
K5P10=0
K5P8=0
K5P15=0
K5L2=0
K5TCV2=0
K5T14=0
K5T3=0
K5T2_1=0
K5T2_2=0
K0P102_1=0
K0T104_2=0
K5F6x=0
K5P13=0
K5P13_1=0

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
        K5TCV2_ans = request.form.get('K5TCV2_ans')
        if str(K5TCV2_ans) != "None":
            send_data("K5TCV2 " + str(K5TCV2_ans))
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

@app.route('/K5T17')
def update_K5T17():
    text = str(K5T17)
    return jsonify(K5T17=text)
@app.route('/K5P10')
def update_K5P10():
    text = str(K5P10)
    return jsonify(K5P10=text)
@app.route('/K5T6')
def update_K5T6():
    text = str(K5T6)
    return jsonify(K5T6=text)
@app.route('/K5P8')
def update_K5P8():
    text = str(K5P8)
    return jsonify(K5P8=text)
@app.route('/K5T15')
def update_K5T15():
    text = str(K5T15)
    return jsonify(K5T15=text)

@app.route('/K5L2')
def update_K5L2():
    text = str(K5L2)
    return jsonify(K5L2=text)
@app.route('/K5TCV2')
def update_K5TCV2():
    text = str(K5TCV2)
    return jsonify(K5TCV2=text)
@app.route('/K5T14')
def update_K5T14():
    text = str(K5T14)
    return jsonify(K5T14=text)
@app.route('/K5T3')
def update_K5T3():
    text = str(K5T3)
    return jsonify(K5T3=text)

@app.route('/K5T2_1')
def update_K5T2_1():
    text = str(K5T2_1)
    return jsonify(K5T2_1=text)

@app.route('/K5T2_2')
def update_K5T2_2():
    text = str(K5T2_2)
    return jsonify(K5T2_2=text)
@app.route('/K0P102_1')
def update_K0P102_1():
    text = str(K0P102_1)
    return jsonify(K0P102_1=text)
@app.route('/K0T104_2')
def update_K0T104_2():
    text = str(K0T104_2)
    return jsonify(K0T104_2=text)
@app.route('/K5F6x')
def update_K5F6x():
    text = str(K5F6x)
    return jsonify(K5F6x=text)
@app.route('/K5P13')
def update_K5P13():
    text = str(K5P13)
    return jsonify(K5P13=text)
@app.route('/K5P13_1')
def update_K5P13_1():
    text = str(K5P13_1)
    return jsonify(K5P13_1=text)

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
