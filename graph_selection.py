from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, 
    QLabel, QMessageBox
)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sns
from car_data_collector import CarScraper

class GraphSelectionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph Selection")
        self.setGeometry(200, 200, 800, 600)
        self.collector = CarScraper()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Graph type selection
        type_layout = QHBoxLayout()
        self.graph_type = QComboBox()
        self.graph_type.addItems(["Scatter Plot", "Bar Chart", "Box Plot", "Histogram"])
        type_layout.addWidget(QLabel("Graph Type:"))
        type_layout.addWidget(self.graph_type)
        layout.addLayout(type_layout)

        # X-axis selection
        x_layout = QHBoxLayout()
        self.x_axis = QComboBox()
        self.x_axis.addItems(["Year", "Price", "Kilometer", "Horsepower", "Engine Size"])
        x_layout.addWidget(QLabel("X-Axis:"))
        x_layout.addWidget(self.x_axis)
        layout.addLayout(x_layout)

        # Y-axis selection
        y_layout = QHBoxLayout()
        self.y_axis = QComboBox()
        self.y_axis.addItems(["Price", "Kilometer", "Horsepower", "Engine Size", "Year"])
        y_layout.addWidget(QLabel("Y-Axis:"))
        y_layout.addWidget(self.y_axis)
        layout.addLayout(y_layout)

        # Generate button
        generate_btn = QPushButton("Generate Graph")
        generate_btn.clicked.connect(self.generate_graph)
        layout.addWidget(generate_btn)

        # Canvas for the graph
        self.figure = plt.figure(figsize=(10, 6))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def generate_graph(self):
        try:
            plt.clf()
            graph_type = self.graph_type.currentText()
            x_feature = self.x_axis.currentText()
            y_feature = self.y_axis.currentText()

            # Get data from collector
            x_data = []
            y_data = []
            
            for car in self.collector.cars:
                x_val = getattr(car, x_feature.lower().replace(" ", ""), None)
                y_val = getattr(car, y_feature.lower().replace(" ", ""), None)
                
                try:
                    x_val = float(x_val)
                    y_val = float(y_val)
                    x_data.append(x_val)
                    y_data.append(y_val)
                except (ValueError, TypeError):
                    continue

            if not x_data or not y_data:
                QMessageBox.warning(self, "Error", "No valid data to plot")
                return

            if graph_type == "Scatter Plot":
                plt.scatter(x_data, y_data, alpha=0.5)
            elif graph_type == "Bar Chart":
                plt.bar(x_data, y_data)
            elif graph_type == "Box Plot":
                plt.boxplot([y_data], labels=[y_feature])
            elif graph_type == "Histogram":
                plt.hist(x_data, bins=30)

            plt.xlabel(x_feature)
            plt.ylabel(y_feature)
            plt.title(f"{graph_type} of {y_feature} vs {x_feature}")
            plt.grid(True)
            self.canvas.draw()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generating graph: {str(e)}") 