#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                              QVBoxLayout, QWidget, QSizePolicy)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spacers & Stretch")
        self.resize(300, 250)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Fixed top"))
        layout.addSpacing(30)
        layout.addWidget(QPushButton("30px gap above"))
        layout.addStretch(1)
        layout.addWidget(QPushButton("Stretch above me"))
        layout.addStretch(2)
        expand_btn = QPushButton("Expanding button (stretch 2 below)")
        layout.addWidget(expand_btn)
        c = QWidget()
        c.setLayout(layout)
        self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
