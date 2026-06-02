#!/usr/bin/env python3
"""Exercises: IPC practice. Run me: python3 exercises.py"""
import sys, socket, json
from PyQt6.QtWidgets import *
from PyQt6.QtNetwork import QLocalServer, QLocalSocket
from PyQt6.QtCore import QTimer

app = QApplication(sys.argv)
SOCK = "/tmp/ex_ipc_test.sock"

# === Ex 1: TCP ping-pong (background server + client) ===
class Ex1(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("TCP Ping"); self.resize(350, 200)
        self.output = QTextEdit(); self.output.setReadOnly(True)
        btn = QPushButton("Send Ping"); btn.clicked.connect(self._ping)
        l = QVBoxLayout(); l.addWidget(self.output); l.addWidget(btn)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(("127.0.0.1", 9998)); self.server.listen(1)
        self.server.setblocking(False)
    def _ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 9998)); s.send(b"ping"); s.close()
        self.output.append("Sent: ping")
        try:
            conn, _ = self.server.accept(); data = conn.recv(1024).decode()
            self.output.append(f"Received: {data}"); conn.close()
        except BlockingIOError: pass

w1 = Ex1(); w1.show()
print("Ex1: TCP ping-pong — send and receive")
QTimer.singleShot(2500, w1.close)
while w1.isVisible(): app.processEvents()
print(f"  Output lines: {w1.output.toPlainText().count(chr(10))}"); print("-" * 40)

# === Ex 2: QLocalServer echo ===
class Ex2(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("IPC Echo"); self.resize(350, 200)
        self.output = QTextEdit(); self.output.setReadOnly(True)
        btn = QPushButton("Send"); btn.clicked.connect(self._send)
        l = QVBoxLayout(); l.addWidget(self.output); l.addWidget(btn)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
        self.server = QLocalServer()
        QLocalServer.removeServer(SOCK)
        self.server.listen(SOCK)
        self.server.newConnection.connect(self._handle)
    def _handle(self):
        sock = self.server.nextPendingConnection()
        sock.readyRead.connect(lambda: self._read(sock))
    def _read(self, sock):
        data = sock.readAll().data().decode()
        self.output.append(f"Server got: {data}")
        sock.write(b"echo"); sock.flush(); sock.disconnectFromServer()
    def _send(self):
        sock = QLocalSocket(); sock.connectToServer(SOCK)
        sock.waitForConnected(1000); sock.write(b"hello"); sock.flush()
        sock.waitForReadyRead(1000)
        self.output.append(f"Client reply: {sock.readAll().data().decode()}")
        sock.disconnectFromServer()

w2 = Ex2(); w2.show()
print("Ex2: QLocalServer echo — send 'hello', get 'echo'")
QTimer.singleShot(2500, w2.close)
while w2.isVisible(): app.processEvents()
print(f"  Output: {w2.output.toPlainText().strip().split(chr(10))}"); print("-" * 40)

# === BONUS: JSON command server ===
class Bonus(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("JSON IPC"); self.resize(400, 250)
        self.output = QTextEdit(); self.output.setReadOnly(True)
        self.server = QLocalServer()
        QLocalServer.removeServer(SOCK)
        self.server.listen(SOCK)
        self.server.newConnection.connect(self._handle)
        btn = QPushButton("Test Commands"); btn.clicked.connect(self._test)
        l = QVBoxLayout(); l.addWidget(self.output); l.addWidget(btn)
        c = QWidget(); c.setLayout(l); self.setCentralWidget(c)
    def _handle(self):
        sock = self.server.nextPendingConnection()
        sock.readyRead.connect(lambda: self._process(sock))
    def _process(self, sock):
        cmd = json.loads(sock.readAll().data().decode())
        r = {"status": "ok", "cmd": cmd.get("cmd")}
        self.output.append(f"Processed: {cmd.get('cmd')}")
        sock.write(json.dumps(r).encode()); sock.flush(); sock.disconnectFromServer()
    def _test(self):
        for cmd in ["hello", "status", "goodbye"]:
            sock = QLocalSocket(); sock.connectToServer(SOCK)
            sock.waitForConnected(1000)
            sock.write(json.dumps({"cmd": cmd}).encode()); sock.flush()
            sock.waitForReadyRead(1000)
            self.output.append(f"Reply: {sock.readAll().data().decode()}")
            sock.disconnectFromServer()

w3 = Bonus(); w3.show()
print("Bonus: JSON command server — hello/status/goodbye")
QTimer.singleShot(3000, w3.close)
while w3.isVisible(): app.processEvents()
print(f"  {w3.output.toPlainText().strip()}"); print("\nDone!"); sys.exit()
