import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import res_rc
from country_football_data_webscraper import get_match_data

class FootballData:
    def __init__(self):
        self.dates = []
        self.locations = []
        self.opponents = []
        self.scores = []
        self.competitions = []

    def filter_by_date_and_result(self, start_year, end_year, win=False, lose=False, draw=False):
        filtered_data = FootballData()
        
        for i in range(len(self.dates)):
            try:
                # Handle different date formats
                date_str = self.dates[i].strip()
                if '.' in date_str:  # dd.mm.yyyy
                    match_year = int(date_str.split('.')[-1])
                elif '-' in date_str:  # dd-mm-yyyy
                    match_year = int(date_str.split('-')[-1])
                elif '/' in date_str:  # dd/mm/yyyy
                    match_year = int(date_str.split('/')[-1])
                else:
                    continue

                if start_year <= match_year <= end_year:
                    score = self.scores[i].strip()
                    
                    # Handle different score formats
                    if '-' in score:
                        try:
                            home_score, away_score = map(int, score.split('-'))
                        except ValueError:
                            # Try cleaning the score string
                            score = ''.join(c for c in score if c.isdigit() or c == '-')
                            if score.count('-') == 1:
                                home_score, away_score = map(int, score.split('-'))
                            else:
                                continue
                        
                        include_match = False
                        if win and home_score > away_score:
                            include_match = True
                        elif lose and home_score < away_score:
                            include_match = True
                        elif draw and home_score == away_score:
                            include_match = True
                        elif not any([win, lose, draw]):  # If no result filter selected
                            include_match = True
                            
                        if include_match:
                            filtered_data.dates.append(self.dates[i])
                            filtered_data.locations.append(self.locations[i])
                            filtered_data.opponents.append(self.opponents[i])
                            filtered_data.scores.append(self.scores[i])
                            filtered_data.competitions.append(self.competitions[i])
            except (ValueError, IndexError) as e:
                print(f"Error processing match: {self.dates[i]} - {self.scores[i]} - {str(e)}")
                continue
                
        return filtered_data

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            f.write("Date,Location,Opponent,Score,League\n")
            for i in range(len(self.dates)):
                # Clean the data before saving
                date = self.dates[i].strip()
                location = self.locations[i].strip().replace(',', ' ')
                opponent = self.opponents[i].strip().replace(',', ' ')
                score = self.scores[i].strip()
                league = self.competitions[i].strip().replace(',', ' ')
                f.write(f"{date},{location},{opponent},{score},{league}\n")

class Ui_MainWindow(object):
    def __init__(self):
        self.countries = ["Turkey", "Spain", "Germany", "England", "France", "Italy", "Belgium"]

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
                                        "    background-color: rgb(237, 237, 237);\n"
                                        "    border-image: url(:/football/football.png);\n"
                                        "}")
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_country = QtWidgets.QLabel(self.centralwidget)
        self.label_country.setGeometry(QtCore.QRect(120, 60, 55, 16))
        self.label_country.setObjectName("label_country")
        self.label_country.setText("Country:") 
        
        self.comboBox_country = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_country.setGeometry(QtCore.QRect(180, 60, 73, 22))
        self.comboBox_country.setStyleSheet("QComboBox {\n"
"    border: 1px solid #8f8f8f;\n"
"    border-radius: 5px;\n"
"    background-color: #f9f9f9;\n"
"    padding: 3px;\n"
"    font-size: 14px;\n"
"}\n")
        
        for country in self.countries:
            self.comboBox_country.addItem(country)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 55, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 100, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 140, 55, 16))
        self.label_4.setObjectName("label_4")
        
        self.comboBox_from = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_from.setGeometry(QtCore.QRect(160, 100, 73, 22))
        self.comboBox_from.setStyleSheet("QComboBox {\n"
"    border: 1px solid #8f8f8f;\n"
"    border-radius: 5px;\n"
"    background-color: #f9f9f9;\n"
"    padding: 3px;\n"
"    font-size: 14px;\n"
"}\n")
        
        self.comboBox_to = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_to.setGeometry(QtCore.QRect(280, 100, 73, 22))
        self.comboBox_to.setStyleSheet("QComboBox {\n"
"    border: 1px solid #8f8f8f;\n"
"    border-radius: 5px;\n"
"    background-color: #f9f9f9;\n"
"    padding: 3px;\n"
"    font-size: 14px;\n"
"}\n")
        
        years = [str(year) for year in range(2000, 2025)]
        self.comboBox_from.addItems(years)
        self.comboBox_to.addItems(years[1:])
        
        self.comboBox_from.currentIndexChanged.connect(self.updateComboBoxTo)
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 150, 295, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        button_style = """
            QPushButton {
                border: 1px solid #8f8f8f;
                border-radius: 5px;
                background-color: #f9f9f9;
                padding: 3px;
                font-size: 14px;
            }
            QPushButton:checked {
                background-color: #d1e0e0;
            }
        """
        
        self.pushButton_win = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_win.setObjectName("pushButton_win")
        self.pushButton_win.setCheckable(True)
        self.pushButton_win.setStyleSheet(button_style)
        self.horizontalLayout.addWidget(self.pushButton_win)
        
        self.pushButton_lose = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_lose.setObjectName("pushButton_lose")
        self.pushButton_lose.setCheckable(True)
        self.pushButton_lose.setStyleSheet(button_style)
        self.horizontalLayout.addWidget(self.pushButton_lose)
        
        self.pushButton_draw = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_draw.setObjectName("pushButton_draw")
        self.pushButton_draw.setCheckable(True)
        self.pushButton_draw.setStyleSheet(button_style)
        self.horizontalLayout.addWidget(self.pushButton_draw)
        
        self.pushButton_run_button = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run_button.setGeometry(QtCore.QRect(220, 260, 93, 28))
        self.pushButton_run_button.setStyleSheet("""
            QPushButton {
                border: 2px solid #8f8f8f;
                border-radius: 10px;
                padding: 5px;
                background-color: #f0f0f0;
            }
            QPushButton:hover {
                background-color: #dcdcdc;
            }
        """)
        
        self.pushButton_run_button.clicked.connect(self.filter_and_save_data)
        
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
        
        # Initialize data after UI setup
        QtCore.QTimer.singleShot(100, self.initialize_data)

    def initialize_data(self):
        try:
            # Show loading message
            msg = QtWidgets.QMessageBox(self.MainWindow)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Scraping match data...\nThis may take a few moments.")
            msg.setWindowTitle("Loading")
            msg.show()
            
            # Scrape data for all countries
            self.scrape_all_data()
            
            # Close loading message
            msg.close()
            
            # Show success message
            QtWidgets.QMessageBox.information(
                self.MainWindow,
                "Success",
                "Match data has been successfully loaded for all countries!"
            )
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self.MainWindow,
                "Error",
                f"Failed to load match data: {str(e)}"
            )

    def scrape_all_data(self):
        for country in self.countries:
            try:
                print(f"Scraping data for {country}...")
                data = get_match_data(country)
                if data:
                    print(f"Got data for {country}, saving to file...")
                    csv_file = f"{country}_matches_standardized.csv"
                    with open(csv_file, 'w', encoding='utf-8') as f:
                        f.write(data)
                    print(f"Saved data for {country}")
                else:
                    print(f"No data received for {country}")
            except Exception as e:
                print(f"Error scraping data for {country}: {str(e)}")
                continue

    def filter_and_save_data(self):
        country = self.comboBox_country.currentText()
        start_year = int(self.comboBox_from.currentText())
        end_year = int(self.comboBox_to.currentText())
        
        win_selected = self.pushButton_win.isChecked()
        lose_selected = self.pushButton_lose.isChecked()
        draw_selected = self.pushButton_draw.isChecked()
        
        # Read the standardized data
        football_data = FootballData()
        csv_file = f"{country}_matches_standardized.csv"
        
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                next(f)  # Skip header
                for line in f:
                    try:
                        if ',' in line:  # Make sure line contains data
                            parts = line.strip().split(',')
                            if len(parts) >= 5:  # Make sure we have all fields
                                date, location, opponent, score, league = parts[:5]
                                football_data.dates.append(date)
                                football_data.locations.append(location)
                                football_data.opponents.append(opponent)
                                football_data.scores.append(score)
                                football_data.competitions.append(league)
                    except ValueError as e:
                        print(f"Error parsing line: {line.strip()} - {str(e)}")
                        continue
            
            if not football_data.dates:
                raise ValueError("No valid data found in the file")
            
            # Filter the data
            filtered_data = football_data.filter_by_date_and_result(
                start_year, end_year, win_selected, lose_selected, draw_selected
            )
            
            if not filtered_data.dates:
                QtWidgets.QMessageBox.warning(
                    self.MainWindow,
                    "No Results",
                    f"No matches found for the selected criteria."
                )
                return
            
            # Save filtered data
            output_file = f"{country}_filtered_{start_year}_{end_year}.csv"
            filtered_data.save_to_csv(output_file)
            
            # Show success message
            QtWidgets.QMessageBox.information(
                self.MainWindow,
                "Success",
                f"Found {len(filtered_data.dates)} matches. Data has been saved to {output_file}"
            )
            
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(
                self.MainWindow,
                "Error",
                f"Could not find data file for {country}. Please make sure the data is scraped first."
            )
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self.MainWindow,
                "Error",
                f"An error occurred: {str(e)}"
            )

    def updateComboBoxTo(self):
        """Update the 'to' combobox to only show years after the selected 'from' year"""
        from_year = int(self.comboBox_from.currentText())
        available_years = [str(year) for year in range(from_year + 1, 2025)]
        self.comboBox_to.clear()
        self.comboBox_to.addItems(available_years)

    def retranslateUi(self, MainWindow):
        """Set up all the text elements in the UI"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Football Match Data"))
        self.label_2.setText(_translate("MainWindow", "From:"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.label_4.setText(_translate("MainWindow", "Results:"))
        self.pushButton_win.setText(_translate("MainWindow", "Win"))
        self.pushButton_lose.setText(_translate("MainWindow", "Lose"))
        self.pushButton_draw.setText(_translate("MainWindow", "Draw"))
        self.pushButton_run_button.setText(_translate("MainWindow", "Save File"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
