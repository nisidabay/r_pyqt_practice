#!/usr/bin/env python3

# PyQt6 — A Hands-On GUI Programming Curriculum
#
# Progressive learning path: from your first window to multi-window applications.
# Each folder is a self-contained module with concepts, exercises, and a project.
#
# Prerequisites:
#   # Create a virtual environment first (recommended):
#   python3 -m venv venv
#   source venv/bin/activate
#   pip install PyQt6
#
#   # Or install system-wide (Arch):
#   sudo pacman -S python-pyqt6
#
#   # Ubuntu:
#   sudo apt install python3-pyqt6
#
# Quick Start:
#   cd 01_hello_window/concept
#   python3 hello_world.py          # Your first window

## Learning Path

| # | Module | What You'll Build |
|---|--------|-------------------|
| 01 | hello_window | Your first window, centered, with a close confirmation |
| 02 | signals_slots | Interactive widgets that respond to clicks and input |
| 03 | widgets | Forms with labels, buttons, inputs, combos, and more |
| 04 | layouts | Arrange widgets with 9 different layout strategies |
| 05 | dialogs | File open/save, color picker, custom dialogs |
| 06 | menus_toolbars | Menu bars, toolbars, status bars, keyboard shortcuts |
| 07 | styling_themes | Dark themes, stylesheets, custom palettes |
| 08 | model_view | Table views, tree views, data-driven widgets |
| 09 | multiwindow | Multiple windows, system tray, settings |

## Project Structure

```
NN_groupname/
├── concept/          # Progressive teaching files (01_*, 02_*, ...)
│   └── README.md     # Quick start, learning path, common patterns
├── exercises.py      # Solved practice problems
└── project/          # One real, self-contained mini-application
```

## Conventions

- PyQt6 only — no Qt licensing issues
- English only — comments explain WHY, not WHAT the code already shows
- Code-first: first 5 lines are running code
- Run any file directly: `python3 filename.py`

## Wayland / niri Users

niri tiles all windows by default, including small PyQt6 tool windows. This makes exercises like `hello_world.py` (300×200) expand to full screen.

**Quick fix** — float the window temporarily while testing:

```bash
# In another terminal, while the PyQt window is focused:
niri msg action move-floating-window-to-workspace
```

**Permanent fix** — add a window rule in `~/.config/niri/config.kdl`:

```kdl
window-rule {
    match title=".*"
    open-floating true
}
```

Remove or scope more tightly after your session. The window title is whatever you pass to `setWindowTitle()` in each script.
