#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *

class SubWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sub Window"); self.resize(300, 200)
        self.setCentralWidget(QLabel("I'm a sub-window"))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main"); self.resize(400, 300)
        self.subs = []
        btn = QPushButton("Open Sub-Window"); btn.clicked.connect(self._open)
        self.setCentralWidget(btn)
    def _open(self):
        sub = SubWindow(self); sub.show(); self.subs.append(sub)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
