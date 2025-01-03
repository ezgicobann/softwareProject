import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from page1 import Ui_MainWindow  # Import Ui_MainWindow from page1.py

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Initialize the application

    # Create the main window instance
    MainWindow = QMainWindow()  
    ui = Ui_MainWindow()  # Instantiate the Ui_MainWindow class from page1.py
    ui.setupUi(MainWindow)  # Setup the UI

    MainWindow.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application event loop
