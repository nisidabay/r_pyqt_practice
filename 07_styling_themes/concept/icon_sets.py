#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QStyle)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Standard Icons"); self.resize(500, 300)
        icons = [n for n in dir(QStyle.StandardPixmap) if n.startswith("SP_")]
        layout = QGridLayout()
        for i, name in enumerate(icons[:28]):
            pixmap = getattr(QStyle.StandardPixmap, name)
            icon = self.style().standardIcon(pixmap)
            btn = QPushButton(icon, name.replace("SP_", ""))
            layout.addWidget(btn, i // 7, i % 7)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow(); window.show(); sys.exit(app.exec())
