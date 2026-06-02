#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal, QObject

class Notifier(QObject):
    message_sent = pyqtSignal(str)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main"); self.resize(350, 200)
        self.notifier = Notifier()
        self.label = QLabel("No messages yet")
        open_btn = QPushButton("Open Sub"); open_btn.clicked.connect(self._open)
        layout = QVBoxLayout(); layout.addWidget(self.label); layout.addWidget(open_btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
    def _open(self):
        sub = QMainWindow(self)
        sub.setWindowTitle("Sub"); sub.resize(250, 150)
        btn = QPushButton("Send Message")
        btn.clicked.connect(lambda: self.notifier.message_sent.emit("Hello from sub!"))
        self.notifier.message_sent.connect(lambda msg: self.label.setText(f"Received: {msg}"))
        sub.setCentralWidget(btn); sub.show()

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
