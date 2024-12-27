import sys
import csv
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QComboBox, QTableWidget, QLabel,
    QVBoxLayout, QHBoxLayout, QWidget, QTableWidgetItem, QFileDialog, QMessageBox, QGridLayout, QCheckBox, QProgressBar
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from graph_selection import GraphSelectionDialog
import pandas as pd



class CarFilterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Car Filtering App")
        self.setGeometry(100, 100, 1000, 600)

        #data
        self.car_data = []

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        #top layout
        top_layout = QGridLayout()
        top_layout.setAlignment(Qt.AlignCenter)

        self.category_dropdown = QComboBox()
        self.category_dropdown.addItems(["Brand", "Series", "Model", "Year", "Price", "Kilometer"])
        self.category_dropdown.currentTextChanged.connect(self.update_dynamic_inputs)

        self.filter_button = QPushButton("Filter")
        self.filter_button.clicked.connect(self.filter_table)

        self.dynamic_widget = QWidget()
        self.dynamic_layout = QHBoxLayout()
        self.dynamic_widget.setLayout(self.dynamic_layout)

        top_layout.addWidget(QLabel("Search Category:"), 0, 0)
        top_layout.addWidget(self.category_dropdown, 0, 1)
        top_layout.addWidget(self.filter_button, 0, 2)
        top_layout.addWidget(self.dynamic_widget, 1, 0, 1, 3)

        main_layout.addLayout(top_layout)

        #search button
        search_layout = QVBoxLayout()

        self.search_button = QPushButton("Search")
        self.search_button.setFixedHeight(40)
        self.search_button.setFixedWidth(200)
        self.search_button.setStyleSheet("margin-bottom: 10px;")
        self.search_button.clicked.connect(self.start_scraping)

        self.detailed_search_checkbox = QCheckBox("Detailed Search (might take longer)")
        self.detailed_search_checkbox.stateChanged.connect(self.toggle_categories)

        search_layout.addWidget(self.search_button, alignment=Qt.AlignHCenter)
        search_layout.addWidget(self.detailed_search_checkbox, alignment=Qt.AlignHCenter)

        main_layout.addLayout(search_layout)

        # loading bar
        self.loading_bar = QProgressBar(self)
        self.loading_bar.setRange(0, 100)
        self.loading_bar.setValue(0)
        self.loading_bar.setTextVisible(True)
        self.loading_bar.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.loading_bar)

        #buttons
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
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Brand", "Series", "Model", "Year", "Price", "Kilometer"
        ])
        main_layout.addWidget(self.table)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.resize(self.table.horizontalHeader().length() + 800, self.table.verticalHeader().length() + 800)

        self.update_dynamic_inputs()

    def toggle_categories(self):
        if self.detailed_search_checkbox.isChecked():
            self.category_dropdown.clear()
            self.category_dropdown.addItems([
                "Brand", "Series", "Model", "Year", "Price", "Kilometer", "Fuel", "Gear", "Bodytype", "Horsepower", "Engine Size", "Colour"
            ])
            self.update_table_headers(detailed=True)
        else:
            self.category_dropdown.clear()
            self.category_dropdown.addItems(["Brand", "Series", "Model", "Year", "Price", "Kilometer"])
            self.update_table_headers(detailed=False)

        self.update_dynamic_inputs()

    def update_table_headers(self, detailed):
        if detailed:
            headers = [
                "Brand", "Series", "Model", "Year", "Price", "Fuel", "Gear", "Kilometer", "Bodytype", "Horsepower", "Engine Size", "Colour"
            ]
        else:
            headers = ["Brand", "Series", "Model", "Year", "Price", "Kilometer"]

        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)

    def update_dynamic_inputs(self):
        while self.dynamic_layout.count():
            child = self.dynamic_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        selected_category = self.category_dropdown.currentText()

        if selected_category in ["Brand", "Series", "Model", "Fuel", "Gear", "Bodytype", "Colour"]:
            dropdown = QComboBox()
            self.dynamic_layout.addWidget(QLabel(f"Choose {selected_category}:"))
            self.dynamic_layout.addWidget(dropdown)
            self.brand_dropdown = dropdown

        elif selected_category in ["Price", "Year", "Kilometer", "Horsepower", "Engine Size"]:
            self.min_input = QLineEdit()
            self.min_input.setPlaceholderText("Min Value")
            self.max_input = QLineEdit()
            self.max_input.setPlaceholderText("Max Value")
            self.dynamic_layout.addWidget(QLabel(f"{selected_category} Interval:"))
            self.dynamic_layout.addWidget(self.min_input)
            self.dynamic_layout.addWidget(self.max_input)

    def start_scraping(self):
        
        #loading bar
        self.loading_bar.setValue(0)
        self.loading_bar.show()

        detailed = self.detailed_search_checkbox.isChecked()
        self.scraping_worker.data_loaded.connect(self.on_data_loaded)
        self.scraping_worker.start()

        # simulate progress bar update
        for i in range(1, 101):
            self.loading_bar.setValue(i)
            self.msleep(50)

    def on_data_loaded(self, data):
        self.loading_bar.setValue(100)
        self.loading_bar.hide()

        self.car_data = data

    def load_data(self, filtered_data=None):
        self.table.setRowCount(0)
        data_to_display = filtered_data if filtered_data else self.car_data

        for row_data in data_to_display:
            row_index = self.table.rowCount()
            self.table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                self.table.setItem(row_index, col_index, QTableWidgetItem(str(cell_data)))

    def filter_table(self):
        pass

    def save_as_csv(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save as CSV", "", "CSV Files (.csv);;All Files ()", options=options
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

    def open_graph_dialog(self):
        dialog = GraphSelectionDialog()
        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarFilterApp()
    window.show()
    sys.exit(app.exec_())
