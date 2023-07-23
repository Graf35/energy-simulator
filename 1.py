from flask import Flask, jsonify
import csv
from flask import render_template
from datetime import datetime

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# Функция для получения значения с сервера
def get_current_time():
    current_time = datetime.now()
    return current_time.strftime("%H:%M:%S")

# Функция для получения текста
def get_text():
    # Здесь можно добавить логику для получения нужного текста
    return "Текст для обновления"

@app.route('/')
def index():
    return render_template('steam_and_water.html')

def update_value():
    time = get_current_time()
    return jsonify(time=time)

# Маршрут сервера, возвращающий значение счетчика
@app.route('/text')
def update_text():
    text = get_text()
    return jsonify(text=text)

if __name__ == "__main__":
    app.run()