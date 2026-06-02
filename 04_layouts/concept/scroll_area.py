#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QScrollArea, QLabel, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QScrollArea")
        self.resize(350, 250)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        inner = QWidget()
        layout = QVBoxLayout(inner)
        for i in range(30):
            layout.addWidget(QLabel(f"Item {i+1}: This is a long line to show horizontal scrolling behavior."))
        layout.addStretch()
        scroll.setWidget(inner)
        self.setCentralWidget(scroll)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
