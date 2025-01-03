from PyQt5 import QtCore, QtGui, QtWidgets
from voiceshow import VoiceShow  #pip install PyQt5 
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 290)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(237, 237, 237);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 20, 91, 61))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("#label_3{\n"
"padding-left: 10px; /* Sol boşluk */\n"
"    padding-right: 10px; /* Sağ boşluk */\n"
"}")
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setPixmap(QtGui.QPixmap(":/user/user.ico"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 80, 161, 61))
        self.label.setStyleSheet("#label\n"
"{\n"
"padding-left: 15px; /* Sol boşluk */\n"
" padding-right: 15px; /* Sağ boşluk */\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 150, 31, 31))
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap(":/password/passworrd.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(170, 150, 141, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #8f8f8f; \n"
"    border-radius: 10px;    \n"
"    padding: 5px;         \n"
"    background-color: #f0f0f0; \n"
"}\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 200, 91, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f8f; \n"
"    border-radius: 10px;    \n"
"    padding: 5px;         \n"
"    background-color: #f0f0f0; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #dcdcdc; \n"
"    \n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Admin Login</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))


class AdminLogin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminLogin, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.pushButton.clicked.connect(self.open_voice_show)
    
    def open_voice_show(self):
        password = self.ui.lineEdit.text()  
        if password == "admin123":
         
            self.voice_window = VoiceShow()  
            self.voice_window.show()
            self.close()  
        else:
        
            QtWidgets.QMessageBox.warning(self, "Error", "Wrong Password")

class VoiceCommand3(QtWidgets.QMainWindow): 
    def __init__(self, parent=None):
        super(VoiceCommand3, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_admin_login)

    def open_admin_login(self):
       
        if not hasattr(self, 'admin_window') or not self.admin_window.isVisible():
            self.admin_window = AdminLogin() 
            self.admin_window.show()
            self.close()  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = VoiceCommand3()  
    window.show()
    sys.exit(app.exec_())
