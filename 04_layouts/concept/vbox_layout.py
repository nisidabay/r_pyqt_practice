#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout")
        self.resize(250, 250)
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Top"))
        layout.addWidget(QPushButton("Middle"))
        layout.addStretch()
        layout.addWidget(QPushButton("Bottom (stretch above)"))
        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
