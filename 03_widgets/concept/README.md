# Widgets — The Building Blocks

Every PyQt6 application is built from these fundamental widgets.

## Quick Start

```bash
python3 labels.py        # QLabel: plain, rich, wrapped, aligned
python3 buttons.py       # QPushButton, QCheckBox, QRadioButton, QButtonGroup
python3 line_edit.py     # QLineEdit: placeholder, password, input mask
python3 text_edit.py     # QTextEdit: multi-line, word count
python3 combo_box.py     # QComboBox: editable dropdown
python3 spin_slider.py   # QSpinBox, QDoubleSpinBox, QSlider, QDial
python3 progress_bar.py  # QProgressBar with timer
python3 list_table.py    # QListWidget, QTableWidget
python3 date_time.py     # QDateEdit, QDateTimeEdit, QCalendarWidget
```

## Learning Path

| File | Widgets | Concept |
|------|---------|---------|
| `labels.py` | QLabel | Text, rich HTML, alignment, word wrap |
| `buttons.py` | QPushButton, QCheckBox, QRadioButton, QButtonGroup | Click signals, toggle, exclusive groups |
| `line_edit.py` | QLineEdit | Placeholder, password echo, input mask, max length |
| `text_edit.py` | QTextEdit | Multi-line text, signals, word count |
| `combo_box.py` | QComboBox | Dropdown list, editable mode |
| `spin_slider.py` | QSpinBox, QDoubleSpinBox, QSlider, QDial | Numeric input, sync between widgets |
| `progress_bar.py` | QProgressBar | Range, timer-driven animation |
| `list_table.py` | QListWidget, QTableWidget | Item selection, table with headers |
| `date_time.py` | QDateEdit, QDateTimeEdit, QCalendarWidget | Date pickers, calendar widget |

## Common Patterns

```python
# QLabel with rich text
label = QLabel("<b>Bold</b> text")
label.setTextFormat(Qt.TextFormat.RichText)

# QLineEdit — password
pw = QLineEdit()
pw.setEchoMode(QLineEdit.EchoMode.Password)

# QCheckBox — toggle
chk = QCheckBox("Enable")
chk.toggled.connect(lambda checked: print(checked))

# QComboBox — editable
combo = QComboBox()
combo.addItems(["A", "B", "C"])
combo.setEditable(True)

# QTableWidget — populate
tw = QTableWidget(3, 2)
tw.setHorizontalHeaderLabels(["Name", "Score"])
tw.setItem(0, 0, QTableWidgetItem("Alice"))
```

## Now Build Your Own

Build a personal info form with: name (QLineEdit), age (QSpinBox), country (QComboBox), subscribe to newsletter (QCheckBox), and a Submit button. Print all values when submitted.
