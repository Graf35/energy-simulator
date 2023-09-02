from flask import Flask, jsonify, render_template, request
import webbrowser
import threading
import Scripts
import logging
from Log import Deman_log
import socket
import time
from pathlib import Path


logger = Deman_log()
config = Scripts.filereader(Path(Path.cwd(), '../../../config.config'))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((config["steam_and_water_screen"], int(config["steam_and_water_screen_port"])))

app = Flask(__name__)


def send_data(data):
    client_socket.send(data.encode())


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
@app.route('/K5PS14_1')
def update_K5PS14_1():
    text = str(K5PS14_1)
    return jsonify(K5PS14_1=text)
@app.route('/K5PS14_2')
def update_K5PS14_2():
    text = str(K5PS14_2)
    return jsonify(K5PS14_2=text)
@app.route('/K5P5_2')
def update_K5P5_2():
    text = str(K5P5_2)
    return jsonify(K5P5_2=text)
@app.route('/K5P5_1')
def update_K5P5_1():
    text = str(K5P5_1)
    return jsonify(K5P5_1=text)
@app.route('/K5Q3')
def update_K5Q3():
    text = str(K5Q3)
    return jsonify(K5Q3=text)
@app.route('/K5L1_1')
def update_K5L1_1():
    text = str(K5L1_1)
    return jsonify(K5L1_1=text)
@app.route('/K5L1_2')
def update_K5L1_2():
    text = str(K5L1_2)
    return jsonify(K5L1_2=text)
@app.route('/K5L1_3')
def update_K5L1_3():
    text = str(K5L1_3)
    return jsonify(K5L1_3=text)
@app.route('/K5L1_4')
def update_K5L1_4():
    text = str(K5L1_4)
    return jsonify(K5L1_4=text)

def connect_to_server():
    server_address = (config["main_server"], int(config["main_server_port"]))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    return client_socket

def reconnect():
    while True:
        try:
            client_socket = connect_to_server()
            logging.info("Соединение востановлено")
            # Если успешно переподключился
            break
        except socket.error:
            # Если произошла ошибка при переподключении
            logging.error("Ошибка при переподключении. Повторная попытка через 5 секунд...")
            time.sleep(5)

def listening_data():
    while True:
        data=client_socket.recv(1024).decode()
        lines=data.split('/n')
        for line in lines:
            if len(line.split())==2:
                variable, value = line.split()
                globals()[variable] = value
            else:
                continue

def chek_connect():
    client_socket = connect_to_server()

    while True:
        try:
            data = client_socket.recv(1024)
            # Обработка полученных данных
        except socket.error:
            logging.error("Потеря соединения. Переподключение...")
            client_socket.close()
            reconnect()



if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    # Привязка callback-функции к очереди сообщений
    listening_deman = threading.Thread(target=listening_data, daemon=True)
    listening_deman.start()
    chek_deman = threading.Thread(target=chek_connect, daemon=True)
    chek_deman.start()
    app.run()
