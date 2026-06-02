#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QColorDialog, QPushButton,
                              QVBoxLayout, QWidget, QLabel)
from PyQt6.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog"); self.resize(300, 200)
        self.label = QLabel("Pick a color →"); self.label.setAutoFillBackground(True)
        btn = QPushButton("Choose Color"); btn.clicked.connect(self._pick)
        layout = QVBoxLayout(); layout.addWidget(self.label); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _pick(self):
        color = QColorDialog.getColor()
        if color.isValid():
            p = self.label.palette()
            p.setColor(QPalette.ColorRole.Window, color)
            self.label.setPalette(p)
            self.label.setText(f"#{color.name()}")

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
