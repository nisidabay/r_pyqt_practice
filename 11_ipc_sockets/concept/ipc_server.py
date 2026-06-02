#!/usr/bin/env python3
"""QLocalServer + QLocalSocket — Qt-native IPC (no TCP, just a Unix socket file)."""
import sys, json
from PyQt6.QtWidgets import *
from PyQt6.QtNetwork import QLocalServer, QLocalSocket

SOCKET = "/tmp/pyqt_ipc_demo.sock"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IPC Server"); self.resize(400, 250)
        self.output = QTextEdit(); self.output.setReadOnly(True)
        self.server = QLocalServer()
        self.server.newConnection.connect(self._on_connection)
        QLocalServer.removeServer(SOCKET)
        self.server.listen(SOCKET)
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Listening on {SOCKET}"))
        layout.addWidget(self.output)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _on_connection(self):
        sock = self.server.nextPendingConnection()
        sock.readyRead.connect(lambda: self._read(sock))

    def _read(self, sock):
        data = sock.readAll().data().decode()
        self.output.append(f"Received: {data}")
        # Echo back
        sock.write(json.dumps({"echo": data}).encode()); sock.flush()
        sock.disconnectFromServer()

    def closeEvent(self, e):
        self.server.close(); QLocalServer.removeServer(SOCKET); e.accept()

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
