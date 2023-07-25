from flask import Flask, jsonify, render_template, request
from datetime import datetime
import webbrowser
import pika
import threading


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# Создание очереди сообщений
channel.queue_declare(queue='data_queue')

K5F5=0
K5LCV1=0

app = Flask(__name__)

# Функция для получения значения с сервера
def get_current_time():
    current_time = datetime.now()
    return current_time.strftime("%H:%M:%S")

# Функция для получения текста
def get_text():
    # Здесь можно добавить логику для получения нужного текста
    return str(K5LCV1)

@app.route('/', methods=['GET', 'POST'])
def index():
    time = datetime.now().strftime('%H:%M:%S')
    if request.method == 'POST':
        K5LCV1 = request.form.get('K5LCV1')
        send_data("K5LCV1 "+str(K5LCV1))
    return render_template('steam_and_water.html', text="1", time=time)

@app.route('/time')
def update_value():
    time = get_current_time()
    return jsonify(time=time)

# Callback-функция для обработки полученных данных
def process_data(data):
    variable, value=data.split()
    globals()[variable]= value

# Callback-функция для обработки полученных сообщений
def callback(ch, method, properties, body):
    process_data(body.decode())

def listening_queue():
    channel.basic_consume(queue='data_queue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

def send_data(data):
    # Отправка данных в RabbitMQ
    channel.basic_publish(exchange='', routing_key='boiler_data', body=str(data))
@app.route('/text')
def update_text():
    text = get_text()
    return jsonify(text=text)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    # Привязка callback-функции к очереди сообщений
    listening_deman = threading.Thread(target=listening_queue, daemon=True)
    listening_deman.start()
    app.run()