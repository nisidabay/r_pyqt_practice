#!/usr/bin/env python3
"""Send a message to the TCP server running on localhost:9999."""
import sys, socket, json
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TCP Client"); self.resize(350, 200)
        self.input = QLineEdit(); self.input.setPlaceholderText("Type a message...")
        self.result = QLabel("(no response yet)")
        send = QPushButton("Send"); send.clicked.connect(self._send)
        layout = QVBoxLayout(); layout.addWidget(self.input)
        layout.addWidget(send); layout.addWidget(self.result)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
    def _send(self):
        msg = self.input.text().strip()
        if not msg: return
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", 9999)); s.send(msg.encode()); s.close()
            self.result.setText(f"Sent: {msg}")
        except ConnectionRefusedError:
            self.result.setText("Error: server not running")

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
