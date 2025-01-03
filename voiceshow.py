
from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(917, 466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_toplam_kayit = QtWidgets.QLabel(self.centralwidget)
        self.label_toplam_kayit.setGeometry(QtCore.QRect(100, 50, 101, 16))
        self.label_toplam_kayit.setObjectName("label_toplam_kayit")
        self.label_kiz_kayit = QtWidgets.QLabel(self.centralwidget)
        self.label_kiz_kayit.setGeometry(QtCore.QRect(145, 90, 81, 16))
        self.label_kiz_kayit.setObjectName("label_kiz_kayit")
        self.label_erkek_kayit = QtWidgets.QLabel(self.centralwidget)
        self.label_erkek_kayit.setGeometry(QtCore.QRect(130, 130, 111, 16))
        self.label_erkek_kayit.setObjectName("label_erkek_kayit")
        self.pushButton_kelime_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kelime_ekle.setGeometry(QtCore.QRect(240, 7, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_kelime_ekle.sizePolicy().hasHeightForWidth())
        self.pushButton_kelime_ekle.setSizePolicy(sizePolicy)
        self.pushButton_kelime_ekle.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_kelime_ekle.setStyleSheet("QPushButton {\n"
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
"\n"
"\n"
"")
        self.pushButton_kelime_ekle.setObjectName("pushButton_kelime_ekle")
        self.pushButton_kelime_sil = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kelime_sil.setGeometry(QtCore.QRect(630, 7, 61, 31))
        self.pushButton_kelime_sil.setStyleSheet("QPushButton {\n"
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
        self.pushButton_kelime_sil.setDefault(False)
        self.pushButton_kelime_sil.setObjectName("pushButton_kelime_sil")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 14, 81, 16))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 114, 16))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 79, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 12, 137, 22))
        self.lineEdit.setStyleSheet("""
QLineEdit {
    border: 2px solid #ddd; /* İnce gri bir kenarlık */
    border-radius: 5px; /* Yuvarlatılmış köşeler */
    padding: 2px; /* Daha küçük bir iç boşluk */
    font-size: 12px; /* Daha okunabilir yazı boyutu */
    color: #333; /* Yazı rengi */
    background-color: #ffffff; /* Beyaz arka plan */
}
""")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 12, 137, 22))
        self.lineEdit_2.setStyleSheet("""
QLineEdit {
    border: 2px solid #ddd; /* İnce gri bir kenarlık */
    border-radius: 5px; /* Yuvarlatılmış köşeler */
    padding: 2px; /* Daha küçük bir iç boşluk */
    font-size: 12px; /* Daha okunabilir yazı boyutu */
    color: #333; /* Yazı rengi */
    background-color: #ffffff; /* Beyaz arka plan */
}
""")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 170, 891, 241))
        self.treeWidget.setStyleSheet("QTreeWidget {\n"
"    background-color: #ffffff; /* Beyaz arka plan rengi */\n"
"    border: 1px solid #ccc; /* İnce gri kenarlık */\n"
"    border-radius: 10px; /* Yuvarlatılmış köşeler */\n"
"    font-size: 14px; /* Yazı büyüklüğü */\n"
"    color: #333; /* Yazı rengi */\n"
"}\n"
"\n"
"")
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setColumnCount(10)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.treeWidget.header().setDefaultSectionSize(110)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(12, 14, 70, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 65, 71, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(480, 65, 137, 22))
        self.lineEdit_3.setStyleSheet("""
QLineEdit {
    border: 2px solid #ddd; /* İnce gri bir kenarlık */
    border-radius: 5px; /* Yuvarlatılmış köşeler */
    padding: 2px; /* Daha küçük bir iç boşluk */
    font-size: 12px; /* Daha okunabilir yazı boyutu */
    color: #333; /* Yazı rengi */
    background-color: #ffffff; /* Beyaz arka plan */
}
""")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_base_path = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_base_path.setGeometry(QtCore.QRect(630, 60, 61, 31))
        self.pushButton_base_path.setStyleSheet("QPushButton {\n"
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
        self.pushButton_base_path.setObjectName("pushButton_base_path")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 26))
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
        self.label_toplam_kayit.setText(_translate("MainWindow", "TextLabel"))
        self.label_kiz_kayit.setText(_translate("MainWindow", "TextLabel"))
        self.label_erkek_kayit.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_kelime_ekle.setText(_translate("MainWindow", "Add"))
        self.pushButton_kelime_sil.setText(_translate("MainWindow", "Delete"))
        self.label.setText(_translate("MainWindow", "Delete Word:"))
        self.label_5.setText(_translate("MainWindow", "Total Male Record:"))
        self.label_3.setText(_translate("MainWindow", "Total Record:"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Işığı"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Alarmı"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Multimedyayı"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Aydınlatmayı"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Parlaklığı"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "İklimlendirmeyi"))
        self.treeWidget.headerItem().setText(6, _translate("MainWindow", "Odayı"))
        self.treeWidget.headerItem().setText(7, _translate("MainWindow", "Fanı"))
        self.treeWidget.headerItem().setText(8, _translate("MainWindow", "Isıtmayı"))
        self.treeWidget.headerItem().setText(9, _translate("MainWindow", "Sıcaklığı"))
        self.label_2.setText(_translate("MainWindow", "Add Word:"))
        self.label_4.setText(_translate("MainWindow", "Total Female Record:"))
        self.label_7.setText(_translate("MainWindow", "Base Path:"))
        self.pushButton_base_path.setText(_translate("MainWindow", "Select"))


class VoiceShow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(VoiceShow, self).__init__()
        self.setupUi(self)
        self.initialize_ui()

    def initialize_ui(self):
        # Butonları işlevlere bağlama
        self.pushButton_kelime_ekle.clicked.connect(self.add_word)
        self.pushButton_kelime_sil.clicked.connect(self.delete_word)
        self.pushButton_base_path.clicked.connect(self.select_base_path)


    def add_word(self):
      
        kelime = self.lineEdit.text()
        if kelime:
            item = QtWidgets.QTreeWidgetItem([kelime])
            self.treeWidget.addTopLevelItem(item)
            self.lineEdit.clear()
        else:
            QtWidgets.QMessageBox.warning(self, "Uyarı", "Kelime alanı boş olamaz!")

    def delete_word(self):
        selected_items = self.treeWidget.selectedItems()
        if selected_items:
            for item in selected_items:
                index = self.treeWidget.indexOfTopLevelItem(item)
                self.treeWidget.takeTopLevelItem(index)
        else:
            QtWidgets.QMessageBox.warning(self, "Uyarı", "Lütfen silmek için bir kelime seçin!")

    def select_base_path(self):
     base_path = QtWidgets.QFileDialog.getExistingDirectory(
        self, "Klasör Seç", QtCore.QDir.homePath()
    )
     if base_path:
             self.lineEdit_3.setText(base_path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    voiceshow = VoiceShow()
    voiceshow.show()
    sys.exit(app.exec_())

