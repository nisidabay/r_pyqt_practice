#!/usr/bin/env python3
"""Two processes talking: server listens, client connects via TCP socket."""
import sys, socket, json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QThread, pyqtSignal

PORT = 9999

class ServerThread(QThread):
    received = pyqtSignal(str)
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", PORT)); s.listen(1)
        while True:
            conn, _ = s.accept()
            data = conn.recv(1024).decode()
            self.received.emit(data)
            conn.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TCP Server"); self.resize(400, 250)
        self.output = QTextEdit(); self.output.setReadOnly(True)
        self.server = ServerThread(); self.server.received.connect(lambda m: self.output.append(f"Received: {m}"))
        self.server.start()
        layout = QVBoxLayout(); layout.addWidget(QLabel(f"Listening on port {PORT}"))
        layout.addWidget(self.output)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
    def closeEvent(self, e): self.server.terminate(); e.accept()

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
