import sys
import csv  
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QComboBox, QTableWidget, QLabel, 
    QVBoxLayout, QHBoxLayout, QWidget, QTableWidgetItem, QFileDialog, QMessageBox, QSlider, QGridLayout, QDateEdit
)
from PyQt5.QtCore import Qt, QDate
from graph_selection import GraphSelectionDialog  
from car_data_collector import (Car, CarScraper)
from time import sleep
import threading
from PyQt5.QtGui import QPixmap
collector = CarScraper()

# main app
class CarFilterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Car Filtering App")
        self.setGeometry(100, 100, 1000, 600)

        # data
        self.car_data = []

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        top_layout = QGridLayout()
        top_layout.setAlignment(Qt.AlignCenter)  

        self.category_dropdown = QComboBox()
        self.category_dropdown.addItems(["Brand","Series","Model","Year","Price","Fuel","Gear","Kilometer","Bodytype","Horsepower","Engine Size","Colour","Traction","Fuel Consumption","Fuel Tank","Paint and Change","From Who"])
        self.category_dropdown.currentTextChanged.connect(self.update_dynamic_inputs)

        self.filter_button = QPushButton("Filter")
        self.filter_button.clicked.connect(self.filter_table)
        
        self.clear_filter_button = QPushButton("Clear Filter")
        self.clear_filter_button.clicked.connect(self.clear_filter)
 
        self.search_button = QPushButton("Search")
        self.pause_button = QPushButton("Pause")
        self.pause_button.setCheckable(True)
        self.pause_button.clicked.connect(self.toggle_scraping)
        self.is_scraping_paused = False

        def search():
            collector.scrapeInBackground()
            thread = threading.Thread(target=self.continuous_Check_Of_Cars)
            thread.start()
            self.pause_button.setEnabled(True)
        self.search_button.clicked.connect(search)
        
        self.dynamic_widget = QWidget()
        self.dynamic_layout = QHBoxLayout()
        self.dynamic_widget.setLayout(self.dynamic_layout)

        top_layout.addWidget(QLabel("Search Category:"), 0, 0)
        top_layout.addWidget(self.category_dropdown, 0, 1)
        top_layout.addWidget(self.filter_button, 0, 2)
        top_layout.addWidget(self.clear_filter_button, 0, 3)
        top_layout.addWidget(self.search_button, 0, 4)
        top_layout.addWidget(self.pause_button, 0, 5)
        top_layout.addWidget(self.dynamic_widget, 1, 0, 1, 6)

        main_layout.addLayout(top_layout)

        # buttons
        button_layout = QHBoxLayout()
        self.save_csv_button = QPushButton("Save as CSV")
        self.save_csv_button.clicked.connect(self.save_as_csv)
        self.get_graph_button = QPushButton("Get Graph")
        self.get_graph_button.clicked.connect(self.open_graph_dialog)
        
        button_layout.addWidget(self.save_csv_button)
        button_layout.addWidget(self.get_graph_button)
        main_layout.addLayout(button_layout)

        # table
        self.table = QTableWidget()
        self.table.setColumnCount(18)
        self.table.setHorizontalHeaderLabels([
            "Ad Date", "Brand","Series","Model","Year","Price","Kilometer","Fuel","Gear","Bodytype","Colour","Horsepower",
            "Engine Size","Traction","Fuel Consumption","Fuel Tank","Paint and Change","From Who"   
        ])
        # Enable sorting
        self.table.setSortingEnabled(True)
        main_layout.addWidget(self.table)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.load_data()  
        self.update_dynamic_inputs()  
        self.image_label = QLabel()

        pixmap = QPixmap("car.png") 
        pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.image_label.setPixmap(pixmap)
        
        self.image_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        top_layout.addWidget(self.image_label, 0, 0, 1, 1)

        main_layout.addLayout(top_layout)

        # Resize the window to fit the table content
        self.resize(self.table.horizontalHeader().length() + 50, self.table.verticalHeader().length() + 800)
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f4f4;
                font-family: Arial, sans-serif;
            }

            QLabel {
                font-size: 14px;
                color: #333;
            }

            QPushButton {
                background-color: #6b6a6a;
                border-radius: 10px;
                color: white;
                padding: 10px 20px;
            }

            QPushButton:hover {
                background-color: #403f3f;
            }

            QComboBox {
                border-radius: 5px;
                border: 2px solid #748a75;
                padding: 5px;
            }

            QComboBox QAbstractItemView {
                background-color: #f4f4f4;
                border-radius: 5px;
            }

            QComboBox::drop-down {
                border: none;
            }

            QTableWidget {
                border-radius: 10px;
                border: 2px solid #ddd;
                background-color: #f9f9f9;
            }

            QTableWidget::item {
                padding: 5px;
                border-radius: 5px;
            }

            QTableWidget::item:selected {
                background-color: #748a75;
                color: white;
            }

            QLineEdit {
                border: 2px solid #748a75;
                border-radius: 10px;
                padding: 5px;
                font-size: 14px;
            }

            QLineEdit:focus {
                border-color: #748a75;
            }

            QComboBox {
                border-radius: 5px;
                border: 2px solid #748a75;
                padding: 5px;
            }
        """)

    def toggle_scraping(self):
        self.is_scraping_paused = not self.is_scraping_paused
        self.pause_button.setText("Resume" if self.is_scraping_paused else "Pause")
        if self.is_scraping_paused:
            collector.pause()
        else:
            collector.resume()

    def update_dynamic_inputs(self):
        while self.dynamic_layout.count():
            child = self.dynamic_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        selected_category = self.category_dropdown.currentText()

        if selected_category in ["Brand","Series","Model", "Fuel","Gear","Bodytype","Colour","Traction","Fuel Consumption","Fuel Tank","Paint and Change","From Who"]:
            dropdown = QComboBox()
            column_mapping = {
                "Brand":1,"Series":2,"Model":3,"Fuel":7,"Gear":8,"Bodytype":9,"Colour":10,
                "Traction":13,"Fuel Consumption":14,"Fuel Tank":15,"Paint and Change":16,"From Who":17
            }
            column_index = column_mapping[selected_category]

            unique_values = set()
            if selected_category == "From Who":
                unique_values = {"Sahibinden", "Galeriden", "belirtilmemiş"}
            else:
                for row in range(self.table.rowCount()):
                    item = self.table.item(row, column_index)
                    if item and item.text().strip():
                        unique_values.add(item.text().strip())
            
            dropdown.addItems(sorted(unique_values))
            self.dynamic_layout.addWidget(QLabel(f"Choose {selected_category}:"))
            self.dynamic_layout.addWidget(dropdown)
            self.brand_dropdown = dropdown

        elif selected_category in ["Price","Year", "Kilometer", "Horsepower","Engine Size"]:
            self.min_input = QLineEdit()
            self.min_input.setPlaceholderText("Min Value")
            self.max_input = QLineEdit()
            self.max_input.setPlaceholderText("Max Value")
            self.dynamic_layout.addWidget(QLabel(f"{selected_category} Interval:"))
            self.dynamic_layout.addWidget(self.min_input)
            self.dynamic_layout.addWidget(self.max_input)

    
    def load_data(self, filtered_data=None):
        self.table.setRowCount(0) 

        if filtered_data:
            # Handle filtered data (which is a list of lists)
            for row_data in filtered_data:
                row_index = self.table.rowCount()
                self.table.insertRow(row_index)
                for col_index, cell_data in enumerate(row_data):
                    self.table.setItem(row_index, col_index, QTableWidgetItem(str(cell_data)))
        else:
            # Handle Car objects from collector
            for car in collector.cars:
                row_data = [
                    car.addate, car.brand, car.series, car.model, car.year, car.price, car.kilometer,
                    car.fuel, car.gear, car.bodytype, car.colour, car.horsepower,
                    car.enginesize, car.traction, car.fuelConsumption, car.fuelTank,
                    car.paintChange, car.fromWho
                ]
                row_index = self.table.rowCount()
                self.table.insertRow(row_index)
                for col_index, cell_data in enumerate(row_data):
                    self.table.setItem(row_index, col_index, QTableWidgetItem(str(cell_data)))

   # dynamic inputs
    def update_dynamic_inputs(self):
        while self.dynamic_layout.count():
            child = self.dynamic_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        selected_category = self.category_dropdown.currentText()

        if selected_category == "Ad Date":
            dropdown = QComboBox()
            unique_dates = set()
            for row in range(self.table.rowCount()):
                item = self.table.item(row, 0)  # Ad Date is in first column
                if item and item.text().strip():
                    try:
                        # Format the date as Month Year
                        date_parts = item.text().split('.')
                        if len(date_parts) >= 2:
                            month_year = f"{date_parts[1]}.{date_parts[2]}"
                            unique_dates.add(month_year)
                    except (IndexError, AttributeError):
                        continue
            
            dropdown.addItems(sorted(unique_dates, reverse=True))  # Most recent dates first
            self.dynamic_layout.addWidget(QLabel("Choose Month:"))
            self.dynamic_layout.addWidget(dropdown)
            self.brand_dropdown = dropdown

        elif selected_category in ["Brand","Series","Model", "Fuel","Gear","Bodytype","Colour","Traction","Fuel Consumption","Fuel Tank","Paint and Change","From Who"]:
            dropdown = QComboBox()
            column_mapping = {
                "Brand":1,"Series":2,"Model":3,"Fuel":7,"Gear":8,"Bodytype":9,"Colour":10,
                "Traction":13,"Fuel Consumption":14,"Fuel Tank":15,"Paint and Change":16,"From Who":17
            }
            column_index = column_mapping[selected_category]

            unique_values = set()
            if selected_category == "From Who":
                unique_values = {"Sahibinden", "Galeriden", "belirtilmemiş"}
            else:
                for row in range(self.table.rowCount()):
                    item = self.table.item(row, column_index)
                    if item and item.text().strip():
                        unique_values.add(item.text().strip())
            
            dropdown.addItems(sorted(unique_values))
            self.dynamic_layout.addWidget(QLabel(f"Choose {selected_category}:"))
            self.dynamic_layout.addWidget(dropdown)
            self.brand_dropdown = dropdown

        elif selected_category in ["Price","Year", "Kilometer", "Horsepower","Engine Size"]:
            self.min_input = QLineEdit()
            self.min_input.setPlaceholderText("Min Value")
            self.max_input = QLineEdit()
            self.max_input.setPlaceholderText("Max Value")
            self.dynamic_layout.addWidget(QLabel(f"{selected_category} Interval:"))
            self.dynamic_layout.addWidget(self.min_input)
            self.dynamic_layout.addWidget(self.max_input)
    
    # filters table fro the selected features
    def filter_table(self):
        filter_category = self.category_dropdown.currentText()
        
        if filter_category in ["Brand","Series","Model","Fuel","Gear","Bodytype","Colour","Traction","Fuel Consumption","Fuel Tank","Paint and Change","From Who"] and hasattr(self, 'brand_dropdown'):
            filter_text = self.brand_dropdown.currentText()
            column_mapping = {
                "Brand":1,"Series":2,"Model":3,"Fuel":7,"Gear":8,"Bodytype":9,"Colour":10,
                "Traction":13,"Fuel Consumption":14,"Fuel Tank":15,"Paint and Change":16,"From Who":17
            }
            filter_column = column_mapping.get(filter_category)
            
            filtered_cars = []
            for row in range(self.table.rowCount()):
                cell_value = self.table.item(row, filter_column).text().strip()
                if cell_value.lower() == filter_text.lower():
                    car_data = []
                    for col in range(self.table.columnCount()):
                        car_data.append(self.table.item(row, col).text())
                    filtered_cars.append(car_data)
            
            self.load_data(filtered_cars)
            return

        elif filter_category in ["Year","Price","Kilometer","Horsepower","Engine Size"] and hasattr(self, 'min_input') and hasattr(self, 'max_input'):
            try:
                min_value = float(self.min_input.text())
                max_value = float(self.max_input.text())
                column_mapping = {"Year":4,"Price":5,"Kilometer":6,"Horsepower":11,"Engine Size":12}
                filter_column = column_mapping.get(filter_category)

                filtered_cars = []
                for row in range(self.table.rowCount()):
                    try:
                        cell_text = self.table.item(row, filter_column).text().strip()
                        
                        if filter_category == "Price":
                            cell_value = float(cell_text.replace(' TL', '').replace('.', ''))
                        elif filter_category == "Horsepower":
                            # Handle ranges and different formats
                            hp_text = cell_text.split(' ')[0].split('-')[0].replace('HP', '').replace('hp', '').strip()
                            cell_value = float(hp_text) if hp_text else 0
                        elif filter_category == "Engine Size":
                            # Handle different engine size formats
                            if 'cc' in cell_text:
                                cell_value = float(cell_text.replace('cc', '').replace(' ', '').strip())
                            elif 'cm3' in cell_text:
                                cell_value = float(cell_text.split('cm3')[0].replace(' ', '').strip())
                            else:
                                cell_value = 0
                        else:
                            cell_value = float(cell_text.replace(',', '').replace('.', ''))

                        if min_value <= cell_value <= max_value:
                            car_data = []
                            for col in range(self.table.columnCount()):
                                car_data.append(self.table.item(row, col).text())
                            filtered_cars.append(car_data)
                    except (ValueError, AttributeError):
                        continue

                self.load_data(filtered_cars)
                return
            except ValueError:
                QMessageBox.warning(self, "Error", "Please enter valid numeric values for min and max")
                return

    #saves as csv
    def save_as_csv(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save as CSV", "", "CSV Files (*.csv);;All Files (*)", options=options
        )

        if file_path:
            try:
                with open(file_path, "w", newline='', encoding="utf-8") as file:
                    writer = csv.writer(file)
                    headers = [self.table.horizontalHeaderItem(i).text() for i in range(self.table.columnCount())]
                    writer.writerow(headers)

                    for row in range(self.table.rowCount()):
                        row_data = [
                            self.table.item(row, col).text() if self.table.item(row, col) else ""
                            for col in range(self.table.columnCount())
                        ]
                        writer.writerow(row_data)
                QMessageBox.information(self, "done!", "datas are saved into csv file")
            except Exception as e:
                QMessageBox.critical(self, "error!", f"some kind of error occured when csv is saving {e}")

    # opens get graph window
    def open_graph_dialog(self):
        dialog = GraphSelectionDialog(self)
        dialog.exec_()

    def continuous_Check_Of_Cars(self):
        previous_lenght = 0
        while True:
            if not self.is_scraping_paused and previous_lenght < len(collector.cars):
                previous_lenght = len(collector.cars)
                self.load_data()
            sleep(10)

    def clear_filter(self):
        self.load_data()  # This will reload all cars
        self.update_dynamic_inputs()  # Update the dropdowns with all values

# main program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarFilterApp()
    window.show()
    sys.exit(app.exec_())
