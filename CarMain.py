import sys
import csv  
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QComboBox, QTableWidget, QLabel, 
    QVBoxLayout, QHBoxLayout, QWidget, QTableWidgetItem, QFileDialog, QMessageBox, QSlider, QGridLayout, QDateEdit
)
from PyQt5.QtCore import Qt, QDate
from graph_selection import GraphSelectionDialog  


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
        self.category_dropdown.addItems(["Brand","Series","Model","Year","Price","Fuel","Gear","Kilometer","Bodytype","Horsepower","Engine Size","Colour"])
        self.category_dropdown.currentTextChanged.connect(self.update_dynamic_inputs)

        self.filter_button = QPushButton("Filter")
        self.filter_button.clicked.connect(self.filter_table)

        self.search_button = QPushButton("Search")
        
        self.dynamic_widget = QWidget()
        self.dynamic_layout = QHBoxLayout()
        self.dynamic_widget.setLayout(self.dynamic_layout)

        top_layout.addWidget(QLabel("Search Category:"), 0, 0)
        top_layout.addWidget(self.category_dropdown, 0, 1)
        top_layout.addWidget(self.filter_button, 0, 2)
        top_layout.addWidget(self.search_button, 0, 3)
        top_layout.addWidget(self.dynamic_widget, 1, 0, 1, 4)

        main_layout.addLayout(top_layout)

        # buttons
        button_layout = QHBoxLayout()
        self.save_csv_button = QPushButton("Save as CSV")
        self.save_csv_button.clicked.connect(self.save_as_csv)  # csv connection
        self.get_graph_button = QPushButton("Get Graph")
        self.get_graph_button.clicked.connect(self.open_graph_dialog)

        button_layout.addWidget(self.save_csv_button)
        button_layout.addWidget(self.get_graph_button)
        main_layout.addLayout(button_layout)

        # table
        self.table = QTableWidget()
        self.table.setColumnCount(12)
        self.table.setHorizontalHeaderLabels([
            "Brand","Series","Model","Year","Price","Fuel","Gear","Kilometer","Bodytype","Horsepower","Engine Size","Colour"
        ])
        main_layout.addWidget(self.table)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.load_data()  
        self.update_dynamic_inputs()  

        # Resize the window to fit the table content
        self.resize(self.table.horizontalHeader().length() + 50, self.table.verticalHeader().length() + 800)

    def load_data(self, filtered_data=None):
        self.table.setRowCount(0)  
        data_to_display = filtered_data if filtered_data else self.car_data

        for row_data in data_to_display:
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

        if selected_category in ["Brand","Series","Model", "Fuel","Gear","Bodytype","Colour"]:
            dropdown = QComboBox()
            column_mapping = {"Brand":0,"Series":1,"Model":2, "Fuel":5,"Gear":6,"Bodytype":8,"Colour":11}
            column_index = column_mapping[selected_category]

            unique_values = sorted(set(row[column_index] for row in self.car_data))
            dropdown.addItems(unique_values)

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
       
        if filter_category in ["Brand","Series","Model","Fuel","Gear","Bodytype","Colour"] and hasattr(self, 'brand_dropdown'):
            filter_text = self.brand_dropdown.currentText().lower()
        elif filter_category in ["Year","Price","Kilometer","Horsepower","Engine Size"] and hasattr(self, 'min_input') and hasattr(self, 'max_input'):
            try:
                min_value = int(self.min_input.text())
                max_value = int(self.max_input.text())
                column_mapping = {"Year":3,"Price":4,"Kilometer":7,"Horsepower":9,"Engine Size":10}
                filter_column = column_mapping.get(filter_category)

                filtered_data = [
                    row for row in self.car_data
                    if min_value <= int(row[filter_column]) <= max_value
                ]
                self.load_data(filtered_data)
                return
            except ValueError:
                QMessageBox.warning(self, "error!", "enter a valid interval")
                return
        else:
            return

        # kategoriyi column indexe eşitleme
        column_mapping = {
             "Brand":0,"Series":1,"Model":2,"Year":3,"Price":4,"Fuel":5,"Gear":6,"Kilometer":7,"Bodytype":8,"Horsepower":9,"Engine Size":10,"Colour":11
        }
        filter_column = column_mapping.get(filter_category)

        # filtreleme
        filtered_data = []
        for row in self.car_data:
            if filter_text in row[filter_column].lower():
                filtered_data.append(row)

        self.load_data(filtered_data)

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
        dialog = GraphSelectionDialog()
        dialog.exec_()

# main program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarFilterApp()
    window.show()
    sys.exit(app.exec_())
