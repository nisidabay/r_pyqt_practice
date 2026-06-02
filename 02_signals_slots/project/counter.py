#!/usr/bin/env python3
"""Counter — Increment and decrement with QLCDNumber display."""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLCDNumber,
    QVBoxLayout, QHBoxLayout, QWidget
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter")
        self.setFixedSize(250, 180)

        self.count = 0

        self.display = QLCDNumber()
        self.display.setDigitCount(6)
        self.display.display(self.count)
        self.display.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        inc_btn = QPushButton("+")
        dec_btn = QPushButton("-")
        reset_btn = QPushButton("Reset")

        inc_btn.clicked.connect(lambda: self._change(1))
        dec_btn.clicked.connect(lambda: self._change(-1))
        reset_btn.clicked.connect(lambda: self._change(-self.count))

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(dec_btn)
        btn_layout.addWidget(reset_btn)
        btn_layout.addWidget(inc_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(btn_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _change(self, delta):
        self.count += delta
        self.display.display(self.count)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
