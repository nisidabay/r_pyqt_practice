#!/usr/bin/env python3
"""Same window, but wrapped in a class — the standard PyQt6 pattern."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        self.resize(300, 200)

        button = QPushButton("Click me")
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
