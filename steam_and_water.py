from flask import Flask, jsonify, request
from equipment.steam_boiler_E5039440gm5 import Steam_boiler
from flask import render_template
from datetime import datetime
import multiprocessing
from tablreader import write_to_csv
from steam_bollerE5039440gm5_run import Testing_window

# bolier = Testing_window("Работа 20Т")
# my_queue = bolier.start_process()

app = Flask(__name__)

# class Steam_and_water():
#     @app.route('/')
#     def __init__(self, parent):
#         if __name__ == '__main__':
#             app.run()
#         text = "Текст для обновления"
#         time = datetime.now().strftime('%H:%M:%S')
#         return render_template('steam_and_water.html', text=text, time=time)


# Функция для получения значения с сервера
def get_current_time():
    current_time = datetime.now()
    return current_time.strftime("%H:%M:%S")

# Функция для получения текста
def get_text():
    # Здесь можно добавить логику для получения нужного текста
    return str(my_queue.get())

@app.route('/', methods=['GET', 'POST'])
def index():
    # text=get_data()
    time = datetime.now().strftime('%H:%M:%S')
    if request.method == 'POST':
        #text = request.form.get('K5LCV1')

        K5LCV1_1 = request.form.get('K5LCV1_1')
    return render_template('steam_and_water.html', text="1", time=time)

@app.route('/time')
def update_value():
    time = get_current_time()
    return jsonify(time=time)

# @app.route('/text')
# def get_data():
#     # Получение данных из очереди
#     result = queue.get()
#     return str(result)



# Маршрут сервера, возвращающий значение счетчика
# @app.route('/text')
# def update_text():
#     text = get_text()
#     return jsonify(text=text)

if __name__ == '__main__':
    # my_queue = queue.Queue()
    # p = multiprocessing.Process(target=bolier.mathematics_process, args=(my_queue,))
    # p.start()
    app.run()
    # driver = webdriver.Chrome()
    # driver.get('http://127.0.0.1:5000')