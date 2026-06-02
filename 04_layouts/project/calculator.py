#!/usr/bin/env python3
"""Calculator Layout — Grid-based calculator interface (no logic, just layout)."""
import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(280, 350)
        main = QVBoxLayout()
        self.display = QLineEdit("0")
        self.display.setAlignment(type(self.display.alignment()).AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")
        main.addWidget(self.display)
        grid = QGridLayout()
        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("C", 3, 2), ("+", 3, 3),
        ]
        for text, row, col in buttons:
            btn = QPushButton(text)
            btn.setFixedSize(55, 45)
            grid.addWidget(btn, row, col)
        equals = QPushButton("=")
        equals.setFixedHeight(45)
        main.addLayout(grid)
        main.addWidget(equals)
        c = QWidget()
        c.setLayout(main)
        self.setCentralWidget(c)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
