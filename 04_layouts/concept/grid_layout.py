#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QGridLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout")
        self.resize(300, 200)
        layout = QGridLayout()
        layout.addWidget(QPushButton("(0,0)"), 0, 0)
        layout.addWidget(QPushButton("(0,1)"), 0, 1)
        layout.addWidget(QPushButton("(0,2)"), 0, 2)
        layout.addWidget(QPushButton("(1,0) spans 2 cols"), 1, 0, 1, 2)
        layout.addWidget(QPushButton("(1,2)"), 1, 2)
        layout.addWidget(QPushButton("(2,0) spans 3 cols"), 2, 0, 1, 3)
        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
