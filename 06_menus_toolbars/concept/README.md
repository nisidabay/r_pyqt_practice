# Menus & Toolbars — Professional Window Shell

Menu bars, context menus, toolbars, status bars, dock widgets, and shared actions.

## Quick Start

```bash
python3 menu_bar.py         # File/Edit/Help menus with shortcuts
python3 context_menu.py     # Right-click context menu
python3 toolbar.py          # Toolbar with standard icons
python3 status_bar.py       # Status bar with char count + cursor position
python3 dock_widgets.py     # Dockable side panel
python3 actions.py          # QAction shared across menu + toolbar
python3 recent_files.py     # File → Open Recent pattern
```

## Learning Path

| File | Concept | Key Pattern |
|------|---------|-------------|
| `menu_bar.py` | QMenuBar, QMenu, QAction | addMenu(), addAction(), setShortcut() |
| `context_menu.py` | Right-click menu | customContextMenuRequested, QMenu::exec() |
| `toolbar.py` | QToolBar + standard icons | addToolBar(), standardIcon() |
| `status_bar.py` | QStatusBar + permanent widgets | addPermanentWidget(), cursorPositionChanged |
| `dock_widgets.py` | QDockWidget | setAllowedAreas(), addDockWidget() |
| `actions.py` | Shared QAction objects | Same QAction in menu AND toolbar |
| `recent_files.py` | QSettings persistence | Open Recent submenu, serialize file list |

## Common Patterns

```python
# Menu with shortcut
act = QAction("&Save", self)
act.setShortcut("Ctrl+S")
act.triggered.connect(self._save)
file_menu.addAction(act)

# Context menu
widget.setContextMenuPolicy(Qt.CustomContextMenu)
widget.customContextMenuRequested.connect(self._context)

# Toolbar
tb = self.addToolBar("Main")
tb.addAction(act)

# Status bar
sb = QStatusBar()
sb.showMessage("Ready", 3000)
self.setStatusBar(sb)
```

## Now Build Your Own

Build a text editor shell with: File menu (New/Open/Save/Exit), Edit menu (Undo/Redo/Cut/Copy/Paste), a toolbar with Open and Save, and a status bar showing character count.
