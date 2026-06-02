#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel")
        self.resize(350, 200)
        layout = QVBoxLayout()
        plain = QLabel("Plain text label")
        rich = QLabel("<b>Bold</b> <i>italic</i> <u>underline</u>")
        rich.setTextFormat(Qt.TextFormat.RichText)
        wrapped = QLabel("A very long sentence that will wrap across multiple lines to demonstrate word wrap.")
        wrapped.setWordWrap(True)
        aligned = QLabel("Right-aligned")
        aligned.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(plain)
        layout.addWidget(rich)
        layout.addWidget(wrapped)
        layout.addWidget(aligned)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
