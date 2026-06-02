#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTextEdit)
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Bar"); self.resize(500, 350)
        self.editor = QTextEdit(); self.setCentralWidget(self.editor)
        file_menu = self.menuBar().addMenu("&File")
        new_act = QAction("&New", self); new_act.setShortcut("Ctrl+N")
        new_act.triggered.connect(self.editor.clear); file_menu.addAction(new_act)
        open_act = QAction("&Open", self); open_act.setShortcut("Ctrl+O")
        open_act.triggered.connect(lambda: print("Open...")); file_menu.addAction(open_act)
        save_act = QAction("&Save", self); save_act.setShortcut("Ctrl+S")
        save_act.triggered.connect(lambda: print("Save...")); file_menu.addAction(save_act)
        file_menu.addSeparator()
        exit_act = QAction("E&xit", self); exit_act.setShortcut("Ctrl+Q")
        exit_act.triggered.connect(self.close); file_menu.addAction(exit_act)
        edit_menu = self.menuBar().addMenu("&Edit")
        undo = QAction("&Undo", self); undo.setShortcut("Ctrl+Z")
        undo.triggered.connect(self.editor.undo); edit_menu.addAction(undo)
        help_menu = self.menuBar().addMenu("&Help")
        about = QAction("&About", self)
        about.triggered.connect(lambda: QMessageBox.about(self, "About", "Menu Demo v1.0"))
        help_menu.addAction(about)

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
