#!/usr/bin/env python3
"""Daemon-like approach: QLocalServer as the interface for a CLI client.
Run: python3 ipc_daemon.py          (starts server)
Then: echo '{"cmd":"hello"}' | python3 ipc_cli.py   (sends command)
"""
import sys, json
from PyQt6.QtWidgets import QApplication
from PyQt6.QtNetwork import QLocalServer, QLocalSocket
from PyQt6.QtCore import QTimer

SOCKET = "/tmp/pyqt_ipc_daemon.sock"

class IPCDaemon:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)
        self.server = QLocalServer()
        self.server.newConnection.connect(self._handle)
        QLocalServer.removeServer(SOCKET)
        self.server.listen(SOCKET)
        self._heartbeat = QTimer()
        self._heartbeat.timeout.connect(lambda: None)
        self._heartbeat.start(1000)
        print(f"IPC Daemon running on {SOCKET}")

    def _handle(self):
        sock = self.server.nextPendingConnection()
        sock.readyRead.connect(lambda: self._process(sock))

    def _process(self, sock):
        data = json.loads(sock.readAll().data().decode())
        cmd = data.get("cmd", "unknown")
        if cmd == "hello": reply = {"status": "ok", "message": "Hello from daemon!"}
        elif cmd == "ping": reply = {"status": "ok", "pong": True}
        elif cmd == "shutdown":
            reply = {"status": "ok", "message": "Shutting down..."}
            sock.write(json.dumps(reply).encode()); sock.flush()
            sock.disconnectFromServer(); self.app.quit(); return
        else: reply = {"status": "error", "message": f"Unknown command: {cmd}"}
        sock.write(json.dumps(reply).encode()); sock.flush()
        sock.disconnectFromServer()

    def run(self): sys.exit(self.app.exec())

if __name__ == "__main__":
    IPCDaemon().run()
