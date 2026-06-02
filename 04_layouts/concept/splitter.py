#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QSplitter, QLabel)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSplitter")
        self.resize(500, 300)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        left = QTextEdit()
        left.setPlaceholderText("Left pane — edit me...")
        right = QTextEdit()
        right.setPlaceholderText("Right pane — drag the divider between us")
        splitter.addWidget(left)
        splitter.addWidget(right)
        splitter.setSizes([250, 250])
        self.setCentralWidget(splitter)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
