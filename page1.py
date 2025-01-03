import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"    background-color: rgb(237, 237, 237);\n"
"    border-image: url(:/software/software.png);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 421, 51))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f8f; \n"
"    border-radius: 10px;    \n"
"    padding: 5px;         \n"
"    background-color: #f0f0f0; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #dcdcdc; \n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/car/car.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(45, 45))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 160, 421, 51))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f8f; \n"
"    border-radius: 10px;    \n"
"    padding: 5px;         \n"
"    background-color: #f0f0f0; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #dcdcdc; \n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/top/top.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(23, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 230, 421, 51))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f8f; \n"
"    border-radius: 10px;    \n"
"    padding: 5px;         \n"
"    background-color: #f0f0f0; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #dcdcdc; \n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mikrofon/mikrofon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Connect button clicks to the methods
        self.pushButton.clicked.connect(self.car_valuation)
        self.pushButton_2.clicked.connect(self.football_prediction)
        self.pushButton_3.clicked.connect(self.voice_command)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Second-Hand Car Valuation"))
        self.pushButton_2.setText(_translate("MainWindow", "Football Match Result Prediction"))
        self.pushButton_3.setText(_translate("MainWindow", "Voice Command Database Creation"))

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
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
