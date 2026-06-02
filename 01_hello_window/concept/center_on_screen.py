#!/usr/bin/env python3
"""Center a window on the primary screen — a real-world pattern."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Centered Window")
        self.resize(300, 200)

        label = QLabel("I'm centered")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        self.center_on_screen()

    def center_on_screen(self):
        screen = self.screen().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
