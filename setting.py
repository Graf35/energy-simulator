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
        self.main_server.setText("Адрес сервера")
        self.main_server_value.setText(self.config["main_server"])
        self.main_server_port.setText("Порт сервера")
        self.main_server_port_value.setText(self.config["main_server_port"])
        self.steam_and_water_screen.setText("Адрес сервера steam_and_water")
        self.steam_and_water_screen_value.setText(self.config["steam_and_water_screen"])
        self.steam_and_water_screen_port.setText("Порт сервера steam_and_water")
        self.steam_and_water_screen_port_value.setText(self.config["steam_and_water_screen_port"])


    def apply_button_clicked(self):
        lines=''
        self.config["developer_mode"]=self.developer_mode_value.text()
        self.config["main_server"]=self.main_server_value.text()
        self.config["main_server_port"] = self.main_server_port_value.text()
        self.config["steam_and_water_screen"] = self.steam_and_water_screen_value.text()
        self.config["steam_and_water_screen_port"] = self.steam_and_water_screen_port_value.text()
        for key in self.config:
           lines+=str (key)+";"+str(self.config[key]+"\n")
        with open("config.config", "w") as file:
            for line in lines:
                if line != "":
                    file.write(line)

