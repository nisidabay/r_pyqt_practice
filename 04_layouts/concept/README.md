# Layouts — Arranging Widgets

Control how widgets are positioned and sized in a window.

## Quick Start

```bash
python3 vbox_layout.py        # Vertical stacking
python3 hbox_layout.py        # Horizontal row
python3 grid_layout.py        # Row × column grid with spans
python3 form_layout.py        # Label-field pairs
python3 nested_layouts.py     # Layouts inside layouts
python3 stacked_layout.py     # Page-based navigation
python3 spacers_stretch.py    # Gaps, stretch, sizing
python3 splitter.py           # Resizable panels
python3 scroll_area.py        # Scrollable content
```

## Learning Path

| File | Layout | Key Feature |
|------|--------|-------------|
| `vbox_layout.py` | QVBoxLayout | addStretch() for push-to-bottom |
| `hbox_layout.py` | QHBoxLayout | addStretch() for centering |
| `grid_layout.py` | QGridLayout | Row/column spans |
| `form_layout.py` | QFormLayout | Automatic label-field pairing |
| `nested_layouts.py` | Composite | VBox of HBoxes |
| `stacked_layout.py` | QStackedLayout | Page switching with prev/next |
| `spacers_stretch.py` | Spacing | addSpacing, stretch ratios |
| `splitter.py` | QSplitter | Draggable dividers |
| `scroll_area.py` | QScrollArea | Overflow into scrollbar |

## Common Patterns

```python
# Vertical stack with push-to-bottom
layout = QVBoxLayout()
layout.addWidget(top)
layout.addStretch()
layout.addWidget(bottom)

# Grid with column span
layout = QGridLayout()
layout.addWidget(wide_widget, 0, 0, 1, 3)  # row=0, col=0, rowspan=1, colspan=3

# Form layout
layout = QFormLayout()
layout.addRow("Name:", QLineEdit())

# Nested: VBox(HBox, HBox)
outer = QVBoxLayout()
outer.addLayout(hbox1)
outer.addLayout(hbox2)

# Stacked pages
stack = QStackedLayout()
stack.addWidget(page1)
stack.addWidget(page2)
stack.setCurrentIndex(1)
```

## Now Build Your Own

Build a settings dialog with two pages (General / Advanced) navigable via QStackedLayout and prev/next buttons. Each page should have at least 2 widgets.
