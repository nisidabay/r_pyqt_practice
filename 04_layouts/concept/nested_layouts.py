#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                              QVBoxLayout, QHBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nested Layouts")
        self.resize(300, 200)
        top_row = QHBoxLayout()
        top_row.addWidget(QPushButton("A"))
        top_row.addWidget(QPushButton("B"))
        bottom_row = QHBoxLayout()
        bottom_row.addWidget(QLabel("Bottom-left"))
        bottom_row.addStretch()
        bottom_row.addWidget(QLabel("Bottom-right"))
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_row)
        main_layout.addStretch()
        main_layout.addLayout(bottom_row)
        c = QWidget()
        c.setLayout(main_layout)
        self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
