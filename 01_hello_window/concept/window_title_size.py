#!/usr/bin/env python3
"""Window properties: title, size, minimum size, and fixed size."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Properties")
        self.resize(400, 300)
        self.setMinimumSize(200, 150)

        label = QLabel("Resize me — but not below 200×150")
        label.setAlignment(
            label.alignment()
            | type(label.alignment()).AlignCenter
        )
        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
