#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QStatusBar, QLabel)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Status Bar"); self.resize(500, 300)
        self.editor = QTextEdit(); self.editor.textChanged.connect(self._update_status)
        self.setCentralWidget(self.editor)
        sb = QStatusBar()
        self.char_label = QLabel("Chars: 0"); self.char_label.setMinimumWidth(80)
        self.pos_label = QLabel("Ln 1, Col 1"); self.pos_label.setMinimumWidth(100)
        sb.addPermanentWidget(self.char_label)
        sb.addPermanentWidget(self.pos_label)
        self.editor.cursorPositionChanged.connect(self._cursor_pos)
        self.setStatusBar(sb)
    def _update_status(self):
        text = self.editor.toPlainText()
        self.char_label.setText(f"Chars: {len(text)}")
    def _cursor_pos(self):
        cursor = self.editor.textCursor()
        self.pos_label.setText(f"Ln {cursor.blockNumber()+1}, Col {cursor.columnNumber()+1}")

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
