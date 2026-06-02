#!/usr/bin/env python3
"""CLI client for the IPC Daemon. Usage: echo '{"cmd":"hello"}' | python3 ipc_cli.py"""
import sys, json
from PyQt6.QtNetwork import QLocalSocket

SOCKET = "/tmp/pyqt_ipc_daemon.sock"

def send(cmd_data):
    sock = QLocalSocket()
    sock.connectToServer(SOCKET)
    if not sock.waitForConnected(2000):
        print(json.dumps({"status": "error", "message": "Daemon not running"}))
        return
    sock.write((json.dumps(cmd_data) + "\n").encode()); sock.flush()
    if sock.waitForReadyRead(2000):
        print(sock.readAll().data().decode())
    sock.disconnectFromServer()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = json.loads(sys.argv[1])
    else:
        data = json.loads(sys.stdin.read())
    send(data)
