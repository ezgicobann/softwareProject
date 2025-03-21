from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from voiceshow import VoiceShow
from admin_login import AdminLogin  
from pvrecorder import PvRecorder
import wave
import struct
import numpy as np
from noisereduce import reduce_noise
import time
import os
import random
import json
from PyQt5 import QtCore, QtGui, QtWidgets

    
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

        # Label for Female
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
        self.label_2.setText("Female")  # Metin değiştirildi

        self.radioButton_kiz = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_kiz.setGeometry(QtCore.QRect(300, 192, 16, 16))
        self.radioButton_kiz.setText("")
        self.radioButton_kiz.setObjectName("radioButton_kiz")

        # Label for Male
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
        self.label_3.setText("Male")  # Metin değiştirildi

        self.radioButton_erkek = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_erkek.setGeometry(QtCore.QRect(462, 192, 16, 16))
        self.radioButton_erkek.setText("")
        self.radioButton_erkek.setObjectName("radioButton_erkek")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 80, 201, 51))
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
        self.label_kelime.setGeometry(QtCore.QRect(390, 75, 291, 51))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(232, 320, 141, 16)) # bottom
        self.label_4.setObjectName("label_4")
        self.label_kelime.setStyleSheet("font-size: 18pt; font-weight: bold;")
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


        ## self.word_list = ["Işığı", "Alarmı", "Multimedyayı", "Aydınlatmayı", "Parlaklığı", "İklimlendirmeyi", "Odayı", "Fanı", "Isıtmayı", "Sıcaklığı"]

        self.pushButton_basla.clicked.connect(self.start_progress)
        self.radioButton_kiz.toggled.connect(self.show_gender)
        self.radioButton_erkek.toggled.connect(self.show_gender)
        self.json_random_num = "unique_id.json"
        
        with open("base_path.json", "r", encoding="utf-8") as file:
            self.base_paths = json.load(file)
            self.base_path = self.base_paths[-1]

    
    def show_gender(self):
        if self.radioButton_kiz.isChecked():
            return "Female"
        
        elif self.radioButton_erkek.isChecked():
            return "Male"
        else:
            return None

    def start_progress(self):
        gender = self.show_gender()

        if gender is None:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Warning! You must choose a gender!")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()
            return
        
        try:
            with open("words.json", "r", encoding="utf-8") as file:
                self.word_list = json.load(file)
                print(self.word_list)

        except FileNotFoundError:
            print("JSON dosyası bulunamadı!")
        except json.JSONDecodeError:
            print("JSON dosyasını okurken bir hata oluştu!")
        except Exception as e:
            print(f"Bir hata oluştu: {str(e)}")
        
        self.edge = len(self.word_list)

        def create_random_num_and_add_list(self):
            random_num = str(random.randint(1000000, 9999999))

            try:

                with open("unique_id.json", "r", encoding="utf-8") as file:
                    try:
                        data = json.load(file)

                    except FileNotFoundError:
                        data = []
                    
            except FileNotFoundError:
                data = []

            while random_num in data:
                random_num = str(random.randint(1000000, 9999999))

            data.append(random_num)  # Yeni numarayı ekle


            with open("unique_id.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            return random_num
        
        random_num = create_random_num_and_add_list(self)
        for i in range(self.edge):
            self.label_kelime.setText(self.word_list[i])

            QtCore.QCoreApplication.processEvents()
            
            if len(PvRecorder.get_available_devices()) > 1:
                recorder  = PvRecorder(device_index=1, frame_length=512)

            else:
                recorder  = PvRecorder(device_index=0, frame_length=512)

            audio = []

            recorder.start()
            print("Recording...")

            start_time = time.time()

            try:
                while True:
                    frame = recorder.read()
                    audio.extend(frame)

                    if time.time() - start_time >= 2.5: # 2.5 saniye kayıt yap
                        print("2.5 seconds passed. Stopping")
                        break
            
            except Exception as e:
                print(f"An error occured: {e}")

            finally:
                recorder.stop()

                audio_np = np.array(audio, dtype=np.int16)
                reduced_audio = reduce_noise(y=audio_np, sr=16000)

                if gender == "Female":

                    target_dir = os.path.join(f"{self.base_path}\Female", self.word_list[i])
                    os.makedirs(target_dir, exist_ok=True)

                    file_path = os.path.join(target_dir, f"{random_num}_Female_{self.word_list[i]}.wav")

                    with wave.open(file_path, "w") as f:
                        f.setparams((1, 2, 16000, 0, "NONE", "NONE"))
                        f.writeframes(struct.pack("h" * len(reduced_audio), *reduced_audio))
                    print(f"Audio saved to {file_path}")

                
                elif gender == "Male":

                    target_dir = os.path.join(f"{self.base_path}\Male", self.word_list[i])
                    os.makedirs(target_dir, exist_ok=True)

                    file_path = os.path.join(target_dir, f"{random_num}_Male_{self.word_list[i]}.wav")

                    with wave.open(file_path, "w") as f:
                        f.setparams((1, 2, 16000, 0, "NONE", "NONE"))
                        f.writeframes(struct.pack("h" * len(reduced_audio), *reduced_audio))
                    print(f"Audio saved to {file_path}")

        self.show_completion_message(unique_id=random_num)


    def show_completion_message(self, unique_id):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Process Completed")
        msg.setText("All words have been processed. What do you want to do?")

        self.save_button = msg.addButton("Save", QMessageBox.AcceptRole)
        self.delete_button = msg.addButton("Delete", QMessageBox.RejectRole)
        self.rerecord_button = msg.addButton("Re-record", QMessageBox.DestructiveRole)

        msg.exec_()

        if msg.clickedButton() == self.save_button:
            self.save_files()

        elif msg.clickedButton() == self.delete_button:
            self.delete_files_by_unique_id(unique_id)

        elif msg.clickedButton() == self.rerecord_button:
            self.delete_files_by_unique_id(unique_id)
            QMessageBox.information(None, "Re-record", "Starting Record in 3 Seconds After This Page is Closed !!.")
            time.sleep(3)
            self.start_progress()

    def save_files(self):
        QMessageBox.information(None, "Save", "Audio files have been saved successfully!")
    

    def delete_files_by_unique_id(self, unique_id):
        base_dir = f"{self.base_path}"
        subfolders = ["Female", "Male"]
        for subfolder in subfolders:
            target_dir = os.path.join(base_dir, subfolder)
            if os.path.exists(target_dir):
                for root, dirs, files in os.walk(target_dir):
                    for file in files:
                        # Eğer dosya adı verilen unique_id ile başlıyorsa sil
                        if file.startswith(unique_id):
                            file_path = os.path.join(root, file)
                            if os.path.isfile(file_path):
                                os.remove(file_path)
                                print(f"Deleted: {file_path}")

        QMessageBox.information(None, "Delete", f"Audio files with unique ID '{unique_id}' have been deleted!")

        
        QMessageBox.information(None, "Delete", "All audio files have been deleted!")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_basla.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Male:</span></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Female:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:600;\">Words to record:</span></p></body></html>"))
        self.pushButton_admin_giris.setText(_translate("MainWindow", "Login"))
        self.label_kelime.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\"></span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Click for admin login</span></p></body></html>"))
        self.actionadmin.setText(_translate("MainWindow", "admin"))
        
        self.admin_window = None 

    def open_admin_login(self):
      
        if self.admin_window is None or not self.admin_window.isVisible():
            self.admin_window = AdminLogin() 
            self.admin_window.show()
        else:
         
            print("Admin giriş penceresi zaten açık.")

if __name__ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
