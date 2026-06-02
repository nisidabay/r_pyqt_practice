#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QStyleFactory, QPushButton,
                              QLabel, QVBoxLayout, QWidget, QComboBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Built-in Styles"); self.resize(300, 200)
        self.label = QLabel("Change the style below")
        self.combo = QComboBox()
        styles = QStyleFactory.keys()
        self.combo.addItems(styles)
        self.combo.currentTextChanged.connect(lambda s: app.setStyle(s))
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(QPushButton("Sample Button"))
        layout.addWidget(QLabel("Available styles:"))
        layout.addWidget(self.combo)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow(); window.show(); sys.exit(app.exec())
