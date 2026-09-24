import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
)

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second window")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Welcome to the second window"))

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main window")
        self.button = QPushButton("Switch window")
        self.button.clicked.connect(self.switch_window)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

    def switch_window(self):
        self.second = SecondWindow()  # keep a reference!
        self.second.show()
        self.close()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())