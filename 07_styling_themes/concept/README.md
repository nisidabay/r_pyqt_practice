# Styling & Themes — Look and Feel

Control how your application looks: built-in styles, custom palettes, and stylesheets.

## Quick Start

```bash
python3 builtin_styles.py       # Switch between system styles (Fusion, Windows, etc.)
python3 fusion_palette.py       # Dark palette with QPalette + Fusion
python3 dark_theme.py           # Complete dark theme definition
python3 stylesheet_basics.py    # CSS-like widget styling
python3 stylesheet_selectors.py # Class selectors, #id, pseudo-states
python3 stylesheet_advanced.py  # Custom scrollbars, deep styling
python3 custom_titlebar.py      # Frameless window + custom title bar
python3 icon_sets.py            # Qt's built-in standard icons
```

## Learning Path

| File | Concept |
|------|---------|
| `builtin_styles.py` | QStyleFactory.keys(), switching styles at runtime |
| `fusion_palette.py` | QPalette ColorRoles: Window, Text, Button, Highlight |
| `dark_theme.py` | Complete palette dictionary pattern |
| `stylesheet_basics.py` | CSS-like setStyleSheet on individual widgets |
| `stylesheet_selectors.py` | #id selectors, :hover/:pressed pseudo-states |
| `stylesheet_advanced.py` | Custom scrollbars, ::handle sub-controls |
| `custom_titlebar.py` | Qt.FramelessWindowHint + custom title bar widget |
| `icon_sets.py` | QStyle.StandardPixmap — 70+ built-in icons |

## Common Patterns

```python
# Dark palette
p = QPalette()
p.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
p.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
app.setStyle("Fusion"); app.setPalette(p)

# Stylesheet with pseudo-states
btn.setStyleSheet("""
    QPushButton { background-color: #4CAF50; color: white; }
    QPushButton:hover { background-color: #45a049; }
    QPushButton:pressed { background-color: #3d8b40; }
""")

# Frameless window
self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
```

## Now Build Your Own

Build a widget gallery that shows a dark-themed form with a toggle button to switch between light and dark modes.
