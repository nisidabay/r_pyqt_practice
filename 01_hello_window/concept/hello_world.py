#!/usr/bin/env python3
"""Minimal PyQt6 window — no class, just three lines of setup."""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Hello World")
button = QPushButton("Click me")
window.setCentralWidget(button)
window.show()

sys.exit(app.exec())
