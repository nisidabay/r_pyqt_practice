#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                              QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stylesheets"); self.resize(300, 200)
        label = QLabel("Styled Label")
        label.setStyleSheet("QLabel { color: white; background-color: #0078D7; padding: 10px; border-radius: 5px; }")
        btn = QPushButton("Styled Button")
        btn.setStyleSheet("""
            QPushButton { background-color: #4CAF50; color: white; padding: 8px; border-radius: 4px; }
            QPushButton:hover { background-color: #45a049; }
            QPushButton:pressed { background-color: #3d8b40; }""")
        layout = QVBoxLayout(); layout.addWidget(label); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow(); window.show(); sys.exit(app.exec())
