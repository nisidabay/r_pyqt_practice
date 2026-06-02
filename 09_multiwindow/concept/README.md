# Multi-Window — Beyond One Window

Multiple windows, modal dialogs, signal communication, system tray, and single-instance enforcement.

## Quick Start

```bash
python3 sub_window.py              # Open multiple child windows
python3 modal_dialog.py            # Modal dialog blocks the parent
python3 signal_between_windows.py  # pyqtSignal across windows
python3 window_manager.py          # Central manager tracks all windows
python3 settings_memory.py         # QSettings: save/restore geometry
python3 system_tray.py             # Minimize to tray, tray menu
python3 single_instance.py         # QSharedMemory: only one instance
```

## Learning Path

| File | Concept |
|------|---------|
| `sub_window.py` | Create and show a second QMainWindow, parent-child lifetime |
| `modal_dialog.py` | setModal(True), .exec(), blocks interaction with parent |
| `signal_between_windows.py` | pyqtSignal + emit across windows |
| `window_manager.py` | Central class that creates, tracks, and destroys windows |
| `settings_memory.py` | QSettings: saveGeometry/restoreGeometry |
| `system_tray.py` | QSystemTrayIcon, hide to tray, tray context menu |
| `single_instance.py` | QSharedMemory to prevent duplicate launches |

## Common Patterns

```python
# Sub-window
sub = QMainWindow(self)  # parent=self for lifetime management
sub.show()

# Modal dialog
dlg = QDialog(self)
dlg.setModal(True)
dlg.exec()  # blocks until closed

# Signal between windows
class Notifier(QObject):
    message = pyqtSignal(str)
n = Notifier()
n.message.connect(lambda msg: label.setText(msg))
n.message.emit("Hello!")

# System tray
tray = QSystemTrayIcon(self)
tray.setContextMenu(menu)
tray.show()

# Single instance
shared = QSharedMemory("unique_key")
if not shared.create(1):
    # Already running
```

## Now Build Your Own

Build a settings window that opens from a main window. Changes in the settings (username, theme) reflect back in the main window via pyqtSignal.
