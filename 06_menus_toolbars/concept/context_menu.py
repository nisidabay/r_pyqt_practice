#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QMenu)
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Context Menu"); self.resize(400, 300)
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Right-click here for context menu...")
        self.editor.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.editor.customContextMenuRequested.connect(self._context_menu)
        self.setCentralWidget(self.editor)
    def _context_menu(self, pos):
        menu = QMenu(self)
        menu.addAction("Cut", self.editor.cut, "Ctrl+X")
        menu.addAction("Copy", self.editor.copy, "Ctrl+C")
        menu.addAction("Paste", self.editor.paste, "Ctrl+V")
        menu.addSeparator()
        menu.addAction("Select All", self.editor.selectAll, "Ctrl+A")
        menu.exec(self.editor.mapToGlobal(pos))

from PyQt6.QtCore import Qt
app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
