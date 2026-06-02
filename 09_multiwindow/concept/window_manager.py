#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *

class WindowManager:
    def __init__(self): self._windows = []
    def create(self, title):
        w = QMainWindow()
        w.setWindowTitle(title); w.resize(250, 150)
        w.setCentralWidget(QLabel(f"Window {len(self._windows)+1}"))
        w.show(); self._windows.append(w)
        return w
    def close_all(self):
        for w in self._windows: w.close()
        self._windows.clear()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Manager"); self.resize(300, 200)
        self.mgr = WindowManager()
        btn = QPushButton("New Window"); btn.clicked.connect(lambda: self.mgr.create("Child"))
        close = QPushButton("Close All"); close.clicked.connect(self.mgr.close_all)
        l = QVBoxLayout(); l.addWidget(btn); l.addWidget(close)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
