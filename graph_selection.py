from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class GraphSelectionDialog(QDialog):
    def __init__(self):
        super().__init__()
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
        self.brand_graph_button = QPushButton("Brand Density Graph")
        self.year_graph_button = QPushButton("Year Graphs")
        self.price_graph_button = QPushButton("Price Graph")

        # add buttons to layout
        layout.addWidget(title)
        layout.addWidget(self.brand_graph_button)
        layout.addWidget(self.year_graph_button)
        layout.addWidget(self.price_graph_button)

        self.setLayout(layout)
