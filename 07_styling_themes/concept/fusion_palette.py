#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                              QVBoxLayout, QWidget, QCheckBox, QProgressBar)
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fusion Palette"); self.resize(300, 250)
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(35, 35, 35))
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        app.setPalette(palette)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Dark Fusion Theme"))
        layout.addWidget(QPushButton("A Button"))
        layout.addWidget(QCheckBox("A Checkbox"))
        bar = QProgressBar(); bar.setValue(65); layout.addWidget(bar)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

app = QApplication(sys.argv); app.setStyle("Fusion")
window = MainWindow(); window.show(); sys.exit(app.exec())
