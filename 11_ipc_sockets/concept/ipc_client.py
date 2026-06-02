#!/usr/bin/env python3
"""Send a message to the QLocalServer and receive a JSON reply."""
import sys, json
from PyQt6.QtWidgets import *
from PyQt6.QtNetwork import QLocalSocket

SOCKET = "/tmp/pyqt_ipc_demo.sock"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IPC Client"); self.resize(350, 200)
        self.input = QLineEdit(); self.input.setPlaceholderText("Message for server...")
        self.result = QLabel("(no response)")
        send = QPushButton("Send"); send.clicked.connect(self._send)
        layout = QVBoxLayout(); layout.addWidget(self.input)
        layout.addWidget(send); layout.addWidget(self.result)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _send(self):
        msg = self.input.text().strip()
        if not msg: return
        sock = QLocalSocket()
        sock.connectToServer(SOCKET)
        if sock.waitForConnected(2000):
            sock.write((json.dumps({"msg": msg}) + "\n").encode()); sock.flush()
            if sock.waitForReadyRead(2000):
                reply = json.loads(sock.readAll().data().decode())
                self.result.setText(f"Server says: {reply.get('echo', '?')}")
            sock.disconnectFromServer()
        else:
            self.result.setText("Error: server not running")

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
