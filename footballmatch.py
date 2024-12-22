from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(479, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
       
        self.label_country = QtWidgets.QLabel(self.centralwidget)
        self.label_country.setGeometry(QtCore.QRect(90, 60, 55, 16))
        self.label_country.setObjectName("label_country")
        self.label_country.setText("Country:")  # Set text for label
        
        self.comboBox_country = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_country.setGeometry(QtCore.QRect(150, 60, 73, 22))
        self.comboBox_country.setObjectName("comboBox_country")
        self.comboBox_country.addItem("Turkey")
        self.comboBox_country.addItem("Spain")
        self.comboBox_country.addItem("Germany")
        self.comboBox_country.addItem("England")
        self.comboBox_country.addItem("France")
        self.comboBox_country.addItem("Italy")
        
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 55, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 100, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 140, 55, 16))
        self.label_4.setObjectName("label_4")
        
        self.comboBox_from = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_from.setGeometry(QtCore.QRect(130, 100, 73, 22))
        self.comboBox_from.setObjectName("comboBox_from")
        
        self.comboBox_to = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_to.setGeometry(QtCore.QRect(250, 100, 73, 22))
        self.comboBox_to.setObjectName("comboBox_to")
        
        years = [str(year) for year in range(2000, 2025)]
        
        self.comboBox_from.addItems(years)
        self.comboBox_to.addItems(years)
        
        self.comboBox_from.currentIndexChanged.connect(self.updateComboBoxTo)
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 150, 295, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.pushButton_win = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_win.setObjectName("pushButton_win")
        self.pushButton_win.setCheckable(True) 
        self.horizontalLayout.addWidget(self.pushButton_win)
        
        self.pushButton_lose = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_lose.setObjectName("pushButton_lose")
        self.pushButton_lose.setCheckable(True) 
        self.horizontalLayout.addWidget(self.pushButton_lose)
        
        self.pushButton_draw = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_draw.setObjectName("pushButton_draw")
        self.pushButton_draw.setCheckable(True)
        self.horizontalLayout.addWidget(self.pushButton_draw)
        
        self.pushButton_run_button = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run_button.setGeometry(QtCore.QRect(190, 250, 93, 28))
        self.pushButton_run_button.setObjectName("pushButton_run_button")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 479, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def updateComboBoxTo(self):
      
        from_year = int(self.comboBox_from.currentText())
        
        available_years = [str(year) for year in range(from_year + 1, 2025)]
        
        self.comboBox_to.clear()
        self.comboBox_to.addItems(available_years)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.label_4.setText(_translate("MainWindow", "Results:"))
        self.pushButton_win.setText(_translate("MainWindow", "Win"))
        self.pushButton_lose.setText(_translate("MainWindow", "Lose"))
        self.pushButton_draw.setText(_translate("MainWindow", "Draw"))
        self.pushButton_run_button.setText(_translate("MainWindow", "Getir"))
      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
