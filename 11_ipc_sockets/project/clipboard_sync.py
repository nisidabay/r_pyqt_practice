#!/usr/bin/env python3
"""Clipboard Sync — Daemon monitors clipboard, CLI client gets/sets remotely.

Usage:
  python3 clipboard_sync.py &            # Start daemon
  echo '{"cmd":"get"}' | python3 ipc_cli.py    # Read clipboard
  echo '{"cmd":"set","text":"Hello"}' | python3 ipc_cli.py  # Write clipboard
"""
import sys, json
from PyQt6.QtWidgets import QApplication
from PyQt6.QtNetwork import QLocalServer, QLocalSocket
from PyQt6.QtCore import QTimer

SOCKET = "/tmp/clipboard_sync.sock"

class ClipboardDaemon:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)
        self.clipboard = self.app.clipboard()
        self.last = self.clipboard.text()
        self.server = QLocalServer()
        self.server.newConnection.connect(self._handle)
        QLocalServer.removeServer(SOCKET)
        self.server.listen(SOCKET)
        self._heartbeat = QTimer()
        self._heartbeat.timeout.connect(self._monitor)
        self._heartbeat.start(500)
        print(f"Clipboard sync daemon on {SOCKET}")

    def _monitor(self):
        current = self.clipboard.text()
        if current != self.last:
            self.last = current
            print(f"Clipboard changed: {current[:50]}...")

    def _handle(self):
        sock = self.server.nextPendingConnection()
        sock.readyRead.connect(lambda: self._process(sock))

    def _process(self, sock):
        data = json.loads(sock.readAll().data().decode())
        cmd = data.get("cmd")
        if cmd == "get":
            text = self.clipboard.text()
            sock.write(json.dumps({"text": text}).encode())
        elif cmd == "set":
            self.clipboard.setText(data.get("text", ""))
            sock.write(json.dumps({"status": "ok"}).encode())
        elif cmd == "shutdown":
            sock.write(json.dumps({"status": "bye"}).encode())
            sock.flush(); sock.disconnectFromServer()
            self.app.quit(); return
        else:
            sock.write(json.dumps({"status": "error", "message": f"Unknown: {cmd}"}).encode())
        sock.flush(); sock.disconnectFromServer()

    def run(self): sys.exit(self.app.exec())

if __name__ == "__main__":
    ClipboardDaemon().run()
