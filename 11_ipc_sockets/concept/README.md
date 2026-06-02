# IPC & Sockets — Processes Talking to Each Other

Two processes communicating: TCP sockets for network, QLocalServer for local IPC.

## Quick Start

```bash
# TCP example (network)
python3 tcp_server.py           # Start server (listens on port 9999)
python3 tcp_client.py           # In another terminal, send messages

# QLocalServer example (Unix socket)
python3 ipc_server.py           # Start server
python3 ipc_client.py           # Send message, get JSON reply

# Daemon + CLI pattern
python3 ipc_daemon.py &         # Start background daemon
echo '{"cmd":"hello"}' | python3 ipc_cli.py    # Send command
echo '{"cmd":"shutdown"}' | python3 ipc_cli.py # Stop daemon
```

## Learning Path

| File | Concept | Transport |
|------|---------|-----------|
| `tcp_server.py` | Accept connections in a thread, emit signals | TCP socket |
| `tcp_client.py` | Connect, send message, display result | TCP socket |
| `ipc_server.py` | QLocalServer, newConnection, readyRead | Unix socket |
| `ipc_client.py` | QLocalSocket, waitForConnected, JSON reply | Unix socket |
| `ipc_daemon.py` | Daemon pattern: listen forever, CLI commands | Unix socket |
| `ipc_cli.py` | Pipe JSON via stdin → send to daemon | Unix socket |

## Common Patterns

```python
# TCP server (threaded)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", PORT)); s.listen(1)
conn, _ = s.accept()
data = conn.recv(1024).decode()

# QLocalServer
server = QLocalServer()
server.removeServer("/tmp/myapp.sock")
server.listen("/tmp/myapp.sock")
server.newConnection.connect(self._handle)

# QLocalSocket client
sock = QLocalSocket()
sock.connectToServer("/tmp/myapp.sock")
sock.waitForConnected(2000)
sock.write(data); sock.flush()
sock.waitForReadyRead(2000)
reply = sock.readAll().data().decode()
```

## Now Build Your Own

Build a clipboard sync tool: a daemon that listens for clipboard changes, a CLI client that can `get`/`set` clipboard contents via IPC.
