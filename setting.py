from PyQt5 import QtWidgets
from PyQt5 import  uic
import Scripts


#Определяем имяи путь до файлас формой окна.
ui=uic.loadUiType("interface/setting.ui")[0]

class Setting(QtWidgets.QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.apply_button.clicked.connect(self.apply_button_clicked)
        self.config = Scripts.filereader("config.config")
        self.developer_mode.setText("Режим разработчика")
        self.developer_mode_value.setText(self.config["developer_mode"])
        self.rabbimq_main_server.setText("Адрес сервера RabbitMQ")
        self.rabbimq_main_server_value.setText(self.config["rabbimq_main_server"])
        self.rabbimq_main_screen.setText("Адрес сервера пользователя RabbitMQ")
        self.rabbimq_main_screen_value.setText(self.config["rabbimq_main_screen"])


    def apply_button_clicked(self):
        lines=''
        self.config["developer_mode"]=self.developer_mode_value.text()
        self.config["rabbimq_main_server"]=self.rabbimq_main_server_value.text()
        for key in self.config:
           lines+=str (key)+";"+str(self.config[key]+"\n")
        with open("config.config", "w") as file:
            for line in lines:
                if line != "":
                    file.write(line)

