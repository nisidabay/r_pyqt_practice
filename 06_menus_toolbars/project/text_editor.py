#!/usr/bin/env python3
"""Text Editor — Full editor with menus, toolbar, status bar, open/save."""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Editor"); self.resize(600, 400)
        self.editor = QTextEdit(); self.setCentralWidget(self.editor)
        self._setup_menus()
        self._setup_toolbar()
        self._setup_statusbar()
        self.editor.textChanged.connect(self._update_status)

    def _setup_menus(self):
        fm = self.menuBar().addMenu("&File")
        for text, slot, short in [
            ("&New", self._new, "Ctrl+N"), ("&Open...", self._open, "Ctrl+O"),
            ("&Save...", self._save, "Ctrl+S"), (None, None, None),
            ("E&xit", self.close, "Ctrl+Q")]:
            if text is None: fm.addSeparator(); continue
            a = QAction(text, self); a.setShortcut(short); a.triggered.connect(slot); fm.addAction(a)
        em = self.menuBar().addMenu("&Edit")
        for text, slot, short in [
            ("&Undo", self.editor.undo, "Ctrl+Z"),
            ("&Redo", self.editor.redo, "Ctrl+Y"), (None, None, None),
            ("Cu&t", self.editor.cut, "Ctrl+X"), ("&Copy", self.editor.copy, "Ctrl+C"),
            ("&Paste", self.editor.paste, "Ctrl+V")]:
            if text is None: em.addSeparator(); continue
            a = QAction(text, self); a.setShortcut(short); a.triggered.connect(slot); em.addAction(a)

    def _setup_toolbar(self):
        tb = self.addToolBar("Main")
        style = self.style()
        for name, slot, icon in [
            ("New", self._new, style.standardIcon(QStyle.StandardPixmap.SP_FileIcon)),
            ("Open", self._open, style.standardIcon(QStyle.StandardPixmap.SP_DialogOpenButton)),
            ("Save", self._save, style.standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton))]:
            tb.addAction(icon, name, slot)

    def _setup_statusbar(self):
        self.sb = QStatusBar()
        self.char_label = QLabel("Chars: 0")
        self.sb.addPermanentWidget(self.char_label)
        self.setStatusBar(self.sb)

    def _update_status(self):
        self.char_label.setText(f"Chars: {len(self.editor.toPlainText())}")

    def _new(self): self.editor.clear()
    def _open(self):
        p, _ = QFileDialog.getOpenFileName(self, "Open", "", "All Files (*)")
        if p:
            with open(p) as f: self.editor.setText(f.read())
            self.sb.showMessage(f"Opened: {p}", 3000)
    def _save(self):
        p, _ = QFileDialog.getSaveFileName(self, "Save", "untitled.txt", "Text (*.txt)")
        if p:
            with open(p, "w") as f: f.write(self.editor.toPlainText())
            self.sb.showMessage(f"Saved: {p}", 3000)

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
