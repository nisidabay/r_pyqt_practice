#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout")
        self.resize(400, 100)
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("Left"))
        layout.addStretch()
        layout.addWidget(QPushButton("Center (stretch both sides)"))
        layout.addStretch()
        layout.addWidget(QPushButton("Right"))
        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
