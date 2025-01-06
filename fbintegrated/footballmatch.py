from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as pd
from datetime import datetime
import os
import traceback
from football_data_scraper import get_match_data

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        
        # Add a text browser to display results
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(90, 290, 620, 250))
        self.textBrowser.setObjectName("textBrowser")
        
        # Add a loading label
        self.loading_label = QtWidgets.QLabel(self.centralwidget)
        self.loading_label.setGeometry(QtCore.QRect(90, 230, 295, 16))
        self.loading_label.setObjectName("loading_label")
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_label.hide()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton_run_button.clicked.connect(self.run_analysis)
    
    def updateComboBoxTo(self):
      
        from_year = int(self.comboBox_from.currentText())
        
        available_years = [str(year) for year in range(from_year + 1, 2025)]
        
        self.comboBox_to.clear()
        self.comboBox_to.addItems(available_years)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Football Match Analysis"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.label_4.setText(_translate("MainWindow", "Results:"))
        self.pushButton_win.setText(_translate("MainWindow", "Win"))
        self.pushButton_lose.setText(_translate("MainWindow", "Lose"))
        self.pushButton_draw.setText(_translate("MainWindow", "Draw"))
        self.pushButton_run_button.setText(_translate("MainWindow", "Getir"))
        self.loading_label.setText(_translate("MainWindow", "Loading data... Please wait."))
      
    def run_analysis(self):
        try:
            # Show loading state
            self.loading_label.show()
            self.pushButton_run_button.setEnabled(False)
            self.textBrowser.setText("Fetching data...")
            QtWidgets.QApplication.processEvents()  # Force UI update
            
            # Get selected values
            country = self.comboBox_country.currentText()
            from_year = int(self.comboBox_from.currentText())
            to_year = int(self.comboBox_to.currentText())
            
            # Get match results selection
            win_selected = self.pushButton_win.isChecked()
            lose_selected = self.pushButton_lose.isChecked()
            draw_selected = self.pushButton_draw.isChecked()
            
            # Get the data
            success = get_match_data(country)
            if not success:
                raise Exception("Failed to fetch match data")
            
            # Read the CSV file
            csv_file = f"{country}_matches_standardized.csv"
            if os.path.exists(csv_file):
                df = pd.read_csv(csv_file)
                
                # Handle date parsing with error handling
                def parse_date(date_str):
                    try:
                        return pd.to_datetime(date_str, format='%d-%m-%Y')
                    except:
                        try:
                            return pd.to_datetime(date_str)
                        except:
                            return None
                
                df['Date'] = df['Date'].apply(parse_date)
                df = df.dropna(subset=['Date'])  # Remove rows with invalid dates
                df['Year'] = df['Date'].dt.year
                
                # Filter by year range
                mask = (df['Year'] >= from_year) & (df['Year'] <= to_year)
                filtered_df = df[mask]
                
                # Filter by match results and prepare detailed output
                result_text = []
                total_matches = len(filtered_df)
                
                result_text.append(f"Analysis for {country} ({from_year}-{to_year})")
                result_text.append(f"Total matches: {total_matches}\n")
                
                if win_selected or lose_selected or draw_selected:
                    # Convert Score column to string type
                    filtered_df['Score'] = filtered_df['Score'].astype(str)
                    
                    if win_selected:
                        wins = filtered_df[filtered_df['Score'].str.contains(r'\d+-\d+', na=False)].copy()
                        wins['Goals_For'] = wins['Score'].str.extract(r'(\d+)-\d+').astype(float)
                        wins['Goals_Against'] = wins['Score'].str.extract(r'\d+-(\d+)').astype(float)
                        wins = wins[wins['Goals_For'] > wins['Goals_Against']]
                        
                        if not wins.empty:
                            result_text.append("=== WINS ===")
                            result_text.append(f"Total Wins: {len(wins)}")
                            for _, match in wins.iterrows():
                                result_text.append(
                                    f"{match['Date'].strftime('%d-%m-%Y')} | "
                                    f"{match['Location']} | "
                                    f"{match['Score']} vs {match['Opponent']} | "
                                    f"{match['Competition']}"
                                )
                            result_text.append("")
                    
                    if lose_selected:
                        losses = filtered_df[filtered_df['Score'].str.contains(r'\d+-\d+', na=False)].copy()
                        losses['Goals_For'] = losses['Score'].str.extract(r'(\d+)-\d+').astype(float)
                        losses['Goals_Against'] = losses['Score'].str.extract(r'\d+-(\d+)').astype(float)
                        losses = losses[losses['Goals_For'] < losses['Goals_Against']]
                        
                        if not losses.empty:
                            result_text.append("=== LOSSES ===")
                            result_text.append(f"Total Losses: {len(losses)}")
                            for _, match in losses.iterrows():
                                result_text.append(
                                    f"{match['Date'].strftime('%d-%m-%Y')} | "
                                    f"{match['Location']} | "
                                    f"{match['Score']} vs {match['Opponent']} | "
                                    f"{match['Competition']}"
                                )
                            result_text.append("")
                    
                    if draw_selected:
                        draws = filtered_df[filtered_df['Score'].str.contains(r'\d+-\d+', na=False)].copy()
                        draws['Goals_For'] = draws['Score'].str.extract(r'(\d+)-\d+').astype(float)
                        draws['Goals_Against'] = draws['Score'].str.extract(r'\d+-(\d+)').astype(float)
                        draws = draws[draws['Goals_For'] == draws['Goals_Against']]
                        
                        if not draws.empty:
                            result_text.append("=== DRAWS ===")
                            result_text.append(f"Total Draws: {len(draws)}")
                            for _, match in draws.iterrows():
                                result_text.append(
                                    f"{match['Date'].strftime('%d-%m-%Y')} | "
                                    f"{match['Location']} | "
                                    f"{match['Score']} vs {match['Opponent']} | "
                                    f"{match['Competition']}"
                                )
                            result_text.append("")
                
                # Display results
                self.textBrowser.setText("\n".join(result_text))
            
            else:
                self.textBrowser.setText(f"Error: Could not find data file for {country}")
                
        except Exception as e:
            error_msg = f"Error occurred: {str(e)}\n{traceback.format_exc()}"
            print(error_msg)  # Print to console for debugging
            self.textBrowser.setText(f"Error occurred: {str(e)}")
        
        finally:
            # Hide loading state
            self.loading_label.hide()
            self.pushButton_run_button.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
