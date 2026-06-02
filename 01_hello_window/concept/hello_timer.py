#!/usr/bin/env python3
"""Window that auto-closes after a delay using QTimer.singleShot."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto-Close")
        self.resize(300, 150)

        label = QLabel("This window closes in 3 seconds...")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        QTimer.singleShot(3000, self.close)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
