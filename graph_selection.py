from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

class GraphSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Select Graph Type")
        self.setGeometry(150, 150, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # title
        title = QLabel("Select Graph Type")
        title.setStyleSheet("font-size: 18px;")
        title.setAlignment(Qt.AlignCenter)

        # buttons
        self.brand_graph_button = QPushButton("Brand Distribution")
        self.brand_graph_button.clicked.connect(self.show_brand_distribution)
        
        self.fuel_graph_button = QPushButton("Fuel Type Distribution")
        self.fuel_graph_button.clicked.connect(self.show_fuel_distribution)
        
        self.gear_graph_button = QPushButton("Gear Type Distribution")
        self.gear_graph_button.clicked.connect(self.show_gear_distribution)
        
        self.year_graph_button = QPushButton("Year Distribution")
        self.year_graph_button.clicked.connect(self.show_year_distribution)
        
        self.price_range_button = QPushButton("Price Range Distribution")
        self.price_range_button.clicked.connect(self.show_price_distribution)

        # add buttons to layout
        layout.addWidget(title)
        layout.addWidget(self.brand_graph_button)
        layout.addWidget(self.fuel_graph_button)
        layout.addWidget(self.gear_graph_button)
        layout.addWidget(self.year_graph_button)
        layout.addWidget(self.price_range_button)

        self.setLayout(layout)

    def show_brand_distribution(self):
        if not self.parent or not self.parent.table:
            return

        brands = []
        for row in range(self.parent.table.rowCount()):
            brand_item = self.parent.table.item(row, 1)  # Brand is in column 1
            if brand_item:
                brands.append(brand_item.text())

        # Count occurrences of each brand
        brand_counts = Counter(brands)
        sorted_brands = sorted(brand_counts.items(), key=lambda x: x[1], reverse=True)
        brand_names = [x[0] for x in sorted_brands]
        counts = [x[1] for x in sorted_brands]

        fig = plt.figure(figsize=(12, 8))
        y_pos = np.arange(len(brand_names))
        plt.barh(y_pos, counts)
        plt.yticks(y_pos, brand_names)
        plt.xlabel('Number of Cars')
        plt.title('Car Brand Distribution')
        plt.tight_layout()
        
        def on_close(event):
            plt.close('all')
            
        fig.canvas.mpl_connect('close_event', on_close)
        plt.show(block=False)
        self.close()  # Close the dialog

    def show_fuel_distribution(self):
        if not self.parent or not self.parent.table:
            return

        fuels = []
        for row in range(self.parent.table.rowCount()):
            fuel_item = self.parent.table.item(row, 7)  # Fuel is in column 7
            if fuel_item:
                fuels.append(fuel_item.text())

        fuel_counts = Counter(fuels)
        fig = plt.figure(figsize=(10, 6))
        plt.pie(fuel_counts.values(), labels=fuel_counts.keys(), autopct='%1.1f%%')
        plt.title('Fuel Type Distribution')
        plt.axis('equal')
        
        def on_close(event):
            plt.close('all')
            
        fig.canvas.mpl_connect('close_event', on_close)
        plt.show(block=False)
        self.close()  # Close the dialog

    def show_gear_distribution(self):
        if not self.parent or not self.parent.table:
            return

        gears = []
        for row in range(self.parent.table.rowCount()):
            gear_item = self.parent.table.item(row, 8)  # Gear is in column 8
            if gear_item:
                gears.append(gear_item.text())

        gear_counts = Counter(gears)
        fig = plt.figure(figsize=(10, 6))
        plt.pie(gear_counts.values(), labels=gear_counts.keys(), autopct='%1.1f%%')
        plt.title('Gear Type Distribution')
        plt.axis('equal')
        
        def on_close(event):
            plt.close('all')
            
        fig.canvas.mpl_connect('close_event', on_close)
        plt.show(block=False)
        self.close()  # Close the dialog

    def show_year_distribution(self):
        if not self.parent or not self.parent.table:
            return

        years = []
        for row in range(self.parent.table.rowCount()):
            year_item = self.parent.table.item(row, 4)  # Year is in column 4
            if year_item:
                try:
                    years.append(int(year_item.text()))
                except ValueError:
                    continue

        fig = plt.figure(figsize=(12, 6))
        plt.hist(years, bins=len(set(years)), edgecolor='black')
        plt.xlabel('Year')
        plt.ylabel('Number of Cars')
        plt.title('Car Year Distribution')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        def on_close(event):
            plt.close('all')
            
        fig.canvas.mpl_connect('close_event', on_close)
        plt.show(block=False)
        self.close()  # Close the dialog

    def show_price_distribution(self):
        if not self.parent or not self.parent.table:
            return

        prices = []
        for row in range(self.parent.table.rowCount()):
            price_item = self.parent.table.item(row, 5)  # Price is in column 5
            if price_item:
                try:
                    price = float(price_item.text().replace(' TL', '').replace('.', ''))
                    prices.append(price)
                except ValueError:
                    continue

        fig = plt.figure(figsize=(12, 6))
        plt.hist(prices, bins=20, edgecolor='black')
        plt.xlabel('Price (TL)')
        plt.ylabel('Number of Cars')
        plt.title('Car Price Distribution')
        plt.ticklabel_format(style='plain', axis='x')
        plt.tight_layout()
        
        def on_close(event):
            plt.close('all')
            
        fig.canvas.mpl_connect('close_event', on_close)
        plt.show(block=False)
        self.close()  # Close the dialog
