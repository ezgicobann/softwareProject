from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from admin_login import AdminLogin  

from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 425)
        MainWindow.setMaximumSize(QtCore.QSize(1126, 832))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("border-color: rgb(189, 189, 189);")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"    background-color: rgb(237, 237, 237);\n"
"    border-image: url(:/voice/voice.png);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_basla = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_basla.setGeometry(QtCore.QRect(227, 270, 236, 28))
        self.pushButton_basla.setMinimumSize(QtCore.QSize(236, 0))
        self.pushButton_basla.setMaximumSize(QtCore.QSize(236, 28))
        self.pushButton_basla.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f8f; \n"
"    border-radius: 10px;    \n"
"    padding: 5px;         \n"
"    background-color: #f0f0f0; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #dcdcdc; \n"
"    \n"
"}")
        self.pushButton_basla.setIconSize(QtCore.QSize(300, 150))
        self.pushButton_basla.setAutoExclusive(False)
        self.pushButton_basla.setObjectName("pushButton_basla")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(390, 184, 74, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(236, 28))
        self.label_3.setObjectName("label_3")
        self.radioButton_kiz = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_kiz.setGeometry(QtCore.QRect(462, 192, 16, 16))
        self.radioButton_kiz.setText("")
        self.radioButton_kiz.setObjectName("radioButton_kiz")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(200, 184, 140, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(236, 28))
        self.label_2.setObjectName("label_2")
        self.radioButton_erkek = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_erkek.setGeometry(QtCore.QRect(300, 192, 44, 16))
        self.radioButton_erkek.setText("")
        self.radioButton_erkek.setObjectName("radioButton_erkek")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(187, 80, 171, 51))
        self.label.setObjectName("label")
        self.pushButton_admin_giris = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_admin_giris.setGeometry(QtCore.QRect(370, 325, 91, 31))
        self.pushButton_admin_giris.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f8f; \n"
"    border-radius: 10px;    \n"
"    padding: 5px;         \n"
"    background-color: #f0f0f0; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #dcdcdc; \n"
"    \n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/login.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_admin_giris.setIcon(icon)
        self.pushButton_admin_giris.setObjectName("pushButton_admin_giris")
        self.pushButton_admin_giris.clicked.connect(self.open_admin_login)
        self.label_kelime = QtWidgets.QLabel(self.centralwidget)
        self.label_kelime.setGeometry(QtCore.QRect(365, 80, 171, 51))
        self.label_kelime.setObjectName("label_kelime")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(225, 315, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 8pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionadmin = QtWidgets.QAction(MainWindow)
        self.actionadmin.setObjectName("actionadmin")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_basla.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Male:</span></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Female:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Words to record:</span></p></body></html>"))
        self.pushButton_admin_giris.setText(_translate("MainWindow", "Login"))
        self.label_kelime.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">TextLabel</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Click for admin login</span></p></body></html>"))
        self.actionadmin.setText(_translate("MainWindow", "admin"))
        
        self.admin_window = None 

    def open_admin_login(self):
      
        if self.admin_window is None or not self.admin_window.isVisible():
            self.admin_window = AdminLogin() 
            self.admin_window.show()
        else:
         
            print("Admin giriş penceresi zaten açık.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

