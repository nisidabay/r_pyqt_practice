#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modal"); self.resize(250, 150)
        self.setModal(True)
        l = QVBoxLayout(self); l.addWidget(QLabel("This dialog blocks the main window"))
        btn = QPushButton("Close"); btn.clicked.connect(self.accept); l.addWidget(btn)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modal Demo"); self.resize(300, 150)
        btn = QPushButton("Open Modal"); btn.clicked.connect(lambda: MyDialog(self).exec())
        self.setCentralWidget(btn)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
