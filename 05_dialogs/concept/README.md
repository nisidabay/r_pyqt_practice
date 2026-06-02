# Dialogs — Asking the User

Modal and standard dialogs for file operations, color selection, user input, and more.

## Quick Start

```bash
python3 message_box.py       # QMessageBox: info, warning, critical, question
python3 file_dialog.py       # QFileDialog: open and save files
python3 color_dialog.py      # QColorDialog: pick color → apply to widget
python3 font_dialog.py       # QFontDialog: choose font → apply
python3 input_dialog.py      # QInputDialog: getText, getInt, getItem
python3 custom_dialog.py     # QDialog subclass with accept/reject
python3 wizard.py            # QWizard: multi-step flow
python3 progress_dialog.py   # QProgressDialog: simulate long operation
```

## Learning Path

| File | Dialog | Key Pattern |
|------|--------|-------------|
| `message_box.py` | QMessageBox.information/warning/critical/question | Static convenience methods |
| `file_dialog.py` | QFileDialog.getOpenFileName/getSaveFileName | Return (path, filter) tuple |
| `color_dialog.py` | QColorDialog.getColor | Check `.isValid()`, apply via QPalette |
| `font_dialog.py` | QFontDialog.getFont | Return (font, ok) tuple |
| `input_dialog.py` | QInputDialog.getText/getInt/getItem | Return (value, ok) tuple |
| `custom_dialog.py` | QDialog + QDialogButtonBox | subclass, accept(), reject() |
| `wizard.py` | QWizard + QWizardPage | addPage(), multi-step |
| `progress_dialog.py` | QProgressDialog | setValue(), wasCanceled(), processEvents() |

## Common Patterns

```python
# Message box with response
r = QMessageBox.question(self, "Title", "Message",
    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
if r == QMessageBox.StandardButton.Yes: ...

# File dialog
path, _ = QFileDialog.getOpenFileName(self, "Open", "", "Text (*.txt)")

# Custom dialog
dlg = MyDialog(self)
if dlg.exec() == QDialog.DialogCode.Accepted:
    data = dlg.get_data()

# Progress dialog
p = QProgressDialog("Working...", "Cancel", 0, 100, self)
for i in range(100):
    if p.wasCanceled(): break
    p.setValue(i); QApplication.processEvents()
```

## Now Build Your Own

Build a simple text editor with File → Open/Save, Edit → change font, and an About dialog. Use QMessageBox, QFileDialog, and QFontDialog.
