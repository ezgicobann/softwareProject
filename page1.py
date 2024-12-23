# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data Collection Software")
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Welcome to our Software Project", self)
        layout.addWidget(label)

        button_layout = QVBoxLayout()

        
        btn_car_valuation = QPushButton("Second-hand Car Valuation", self)
        btn_car_valuation.clicked.connect(self.car_valuation)
        button_layout.addWidget(btn_car_valuation)

      
        btn_football_prediction = QPushButton("Football Match Result Prediction", self)
        btn_football_prediction.clicked.connect(self.football_prediction)
        button_layout.addWidget(btn_football_prediction)

       
        btn_voice_command = QPushButton("Voice Command Database Creation", self)
        btn_voice_command.clicked.connect(self.voice_command)
        button_layout.addWidget(btn_voice_command)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def car_valuation(self):
        from CarMain import CarFilterApp  
        self.CarFilter_window = QtWidgets.QMainWindow()  
        self.ui = CarFilterApp()  
        self.ui.show()  



    def football_prediction(self):
       
        from footballmatch import Ui_MainWindow  
        self.football_window = QtWidgets.QMainWindow() 
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self.football_window)  
        self.football_window.show()  

    def voice_command(self):
       
        from voicecommand3 import Ui_MainWindow 
        self.voice_command_window = QtWidgets.QMainWindow() 
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self.voice_command_window) 
        self.voice_command_window.show() 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
