from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from admin_login import AdminLogin  # AdminLogin sınıfını içe aktar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 455)
        MainWindow.setMaximumSize(QtCore.QSize(1126, 832))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_kaydet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kaydet.setEnabled(True)
        self.pushButton_kaydet.setGeometry(QtCore.QRect(350, 250, 236, 28))
        self.pushButton_kaydet.setMinimumSize(QtCore.QSize(236, 0))
        self.pushButton_kaydet.setMaximumSize(QtCore.QSize(236, 28))
        self.pushButton_kaydet.setIconSize(QtCore.QSize(300, 150))
        self.pushButton_kaydet.setObjectName("pushButton_kaydet")
        self.pushButton_basla = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_basla.setGeometry(QtCore.QRect(90, 250, 236, 28))
        self.pushButton_basla.setMinimumSize(QtCore.QSize(236, 0))
        self.pushButton_basla.setMaximumSize(QtCore.QSize(236, 28))
        self.pushButton_basla.setIconSize(QtCore.QSize(300, 150))
        self.pushButton_basla.setAutoExclusive(False)
        self.pushButton_basla.setObjectName("pushButton_basla")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(370, 160, 74, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(236, 28))
        self.label_3.setObjectName("label_3")
        self.radioButton_kiz = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_kiz.setGeometry(QtCore.QRect(460, 167, 16, 16))
        self.radioButton_kiz.setText("")
        self.radioButton_kiz.setObjectName("radioButton_kiz")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(220, 160, 140, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(236, 28))
        self.label_2.setObjectName("label_2")
        self.radioButton_erkek = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_erkek.setGeometry(QtCore.QRect(280, 167, 44, 16))
        self.radioButton_erkek.setText("")
        self.radioButton_erkek.setObjectName("radioButton_erkek")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 80, 171, 22))
        self.label.setObjectName("label")
        self.lineEdit_ = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_.setGeometry(QtCore.QRect(280, 80, 315, 22))
        self.lineEdit_.setObjectName("lineEdit_")
        self.pushButton_admin_giris = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_admin_giris.setGeometry(QtCore.QRect(320, 365, 93, 28))
        self.pushButton_admin_giris.setObjectName("pushButton_admin_giris")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 370, 108, 16))
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
        self.pushButton_kaydet.setText(_translate("MainWindow", "Kaydet"))
        self.pushButton_basla.setText(_translate("MainWindow", "Başla"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Erkek:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Kız:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Söylenecek Kelime: </span></p></body></html>"))
        self.pushButton_admin_giris.setText(_translate("MainWindow", "Giriş"))
        self.label_4.setText(_translate("MainWindow", "Admin girişi için tıklayın "))
        self.actionadmin.setText(_translate("MainWindow", "admin"))

     
        self.pushButton_admin_giris.clicked.connect(self.open_admin_login)

        
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
