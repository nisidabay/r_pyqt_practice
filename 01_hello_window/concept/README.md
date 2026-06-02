# Hello Window — Your First PyQt6 Window

The foundation: create, show, and control a window.

## Quick Start

```bash
python3 hello_world.py          # Bare minimum — no class
python3 hello_class.py          # Same but with a MainWindow class
python3 window_title_size.py    # Title, size, minimum size
python3 center_on_screen.py     # Center on the primary monitor
python3 close_event.py          # Ask before quitting
python3 hello_timer.py          # Auto-close after 3 seconds
```

## Learning Path

| File | Concept | Run |
|------|---------|-----|
| `hello_world.py` | QApplication, QMainWindow, show, exec | `python3 hello_world.py` |
| `hello_class.py` | Subclass QMainWindow, __init__ pattern | `python3 hello_class.py` |
| `window_title_size.py` | setWindowTitle, resize, setMinimumSize | `python3 window_title_size.py` |
| `center_on_screen.py` | screen().availableGeometry(), move | `python3 center_on_screen.py` |
| `close_event.py` | Override closeEvent, QMessageBox question | `python3 close_event.py` |
| `hello_timer.py` | QTimer.singleShot for delayed actions | `python3 hello_timer.py` |

## Common Patterns

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.resize(400, 300)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
```

## Now Build Your Own

Create a window that opens at 500×300 pixels, centered on screen, with the title "My App" and a label that reads "Ready." — closes after 5 seconds automatically.
