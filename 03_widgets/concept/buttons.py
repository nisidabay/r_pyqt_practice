#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QCheckBox,
                              QRadioButton, QButtonGroup, QVBoxLayout, QWidget, QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons")
        self.resize(300, 280)
        self.status = QLabel("Push a button")
        btn = QPushButton("Click Me")
        btn.clicked.connect(lambda: self.status.setText("Button clicked!"))
        chk = QCheckBox("Enable feature")
        chk.toggled.connect(lambda v: self.status.setText(f"Checkbox: {v}"))
        radio1 = QRadioButton("Option A")
        radio2 = QRadioButton("Option B")
        group = QButtonGroup(self)
        group.addButton(radio1, 0)
        group.addButton(radio2, 1)
        group.idClicked.connect(lambda i: self.status.setText(f"Radio: option {i}"))
        layout = QVBoxLayout()
        layout.addWidget(self.status)
        layout.addWidget(btn)
        layout.addWidget(chk)
        layout.addWidget(radio1)
        layout.addWidget(radio2)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
