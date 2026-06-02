# Signals & Slots — Making Things Happen

Qt's core communication mechanism: widgets emit signals, slots handle them.

## Quick Start

```bash
python3 signal_basics.py       # Button click → disable button
python3 lambda_slots.py        # Inline lambda slots
python3 named_slots.py         # Named methods with @pyqtSlot
python3 signal_arguments.py    # Signals that carry data
python3 sender_method.py       # Identify which widget fired
python3 custom_signal.py       # Define your own signals
```

## Learning Path

| File | Concept | Run |
|------|---------|-----|
| `signal_basics.py` | widget.signal.connect(slot) | `python3 signal_basics.py` |
| `lambda_slots.py` | Inline lambda for simple actions | `python3 lambda_slots.py` |
| `named_slots.py` | Named methods, @pyqtSlot decorator | `python3 named_slots.py` |
| `signal_arguments.py` | textChanged, valueChanged carry data | `python3 signal_arguments.py` |
| `sender_method.py` | self.sender() identifies the source | `python3 sender_method.py` |
| `custom_signal.py` | pyqtSignal() for custom communication | `python3 custom_signal.py` |

## Common Patterns

```python
# Button click
button.clicked.connect(self.on_clicked)

# Inline lambda
button.clicked.connect(lambda: self.label.setText("Clicked!"))

# Signal with data
slider.valueChanged.connect(self.on_value_changed)
# def on_value_changed(self, value): ...

# Identify sender
def on_any_button(self):
    sender = self.sender()  # returns the QPushButton that was clicked

# Custom signal
class Model(QObject):
    data_changed = pyqtSignal(str)
    # ...
    self.data_changed.emit("new data")
```

## Now Build Your Own

Build a window with a text input and a "Submit" button. When clicked, copy the input text to a label below and clear the input field.
