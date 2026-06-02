#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit")
        self.resize(350, 220)
        self.label = QLabel("Output appears here")
        pw = QLineEdit()
        pw.setPlaceholderText("Password mode")
        pw.setEchoMode(QLineEdit.EchoMode.Password)
        pw.textChanged.connect(lambda t: self.label.setText(f"Password: {'*' * len(t)}"))
        masked = QLineEdit()
        masked.setPlaceholderText("Date mask: __-__-____")
        masked.setInputMask("99-99-9999")
        normal = QLineEdit()
        normal.setPlaceholderText("Normal input — max 20 chars")
        normal.setMaxLength(20)
        normal.textChanged.connect(lambda t: self.label.setText(f"Input: {t}"))
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(normal)
        layout.addWidget(pw)
        layout.addWidget(masked)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
