#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QFormLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout")
        self.resize(350, 200)
        layout = QFormLayout()
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Email:", QLineEdit())
        layout.addRow("Phone:", QLineEdit())
        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
