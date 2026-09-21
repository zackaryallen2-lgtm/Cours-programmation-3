import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog,
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
)


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        # Passing 'parent' centers the dialog over the main window
        super().__init__(parent)
        self.setWindowTitle("Custom Dialog Form")

        # 1. Create layout and widgets
        layout = QVBoxLayout(self)

        self.label = QLabel("Please enter your name:")
        self.input_field = QLineEdit()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)

        # 2. Add action buttons (OK / Cancel)
        button_layout = QHBoxLayout()
        self.btn_ok = QPushButton("OK")
        self.btn_cancel = QPushButton("Cancel")

        button_layout.addWidget(self.btn_ok)
        button_layout.addWidget(self.btn_cancel)
        layout.addLayout(button_layout)

        # 3. Connect buttons to built-in QDialog slots
        self.btn_ok.clicked.connect(self.accept)  # Closes dialog, returns QDialog.Accepted (1)
        self.btn_cancel.clicked.connect(self.reject)  # Closes dialog, returns QDialog.Rejected (0)

    def get_data(self):
        return self.input_field.text()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Application Window")
        self.resize(300, 200)

        # Main window button to trigger the dialog
        self.button = QPushButton("Open Form Dialog")
        self.button.clicked.connect(self.launch_dialog)
        self.setCentralWidget(self.button)

    def launch_dialog(self):
        # Instantiate the dialog passing 'self' as parent
        dialog = CustomDialog(self)

        # exec() blocks the parent UI and starts a local event loop
        result = dialog.exec()

        if result == QDialog.Accepted:
            user_input = dialog.get_data()
            print(f"User saved data: {user_input}")
        else:
            print("User cancelled the dialog.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
