#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QSettings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recent Files"); self.resize(500, 350)
        self.settings = QSettings("MyApp", "TextEditor")
        self.editor = QTextEdit(); self.setCentralWidget(self.editor)
        self.recent = self.settings.value("recentFiles", [])
        file_menu = self.menuBar().addMenu("&File")
        open_act = QAction("&Open...", self); open_act.setShortcut("Ctrl+O")
        open_act.triggered.connect(self._open); file_menu.addAction(open_act)
        self.recent_menu = file_menu.addMenu("Open Recent")
        self._update_recent()
        file_menu.addSeparator()
        exit_act = QAction("E&xit", self); exit_act.setShortcut("Ctrl+Q")
        exit_act.triggered.connect(self.close); file_menu.addAction(exit_act)

    def _open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open", "", "All Files (*)")
        if path:
            with open(path) as f: self.editor.setText(f.read())
            if path not in self.recent:
                self.recent.insert(0, path)
                self.recent = self.recent[:5]
                self.settings.setValue("recentFiles", self.recent)
                self._update_recent()

    def _update_recent(self):
        self.recent_menu.clear()
        if self.recent:
            for p in self.recent:
                act = QAction(p, self)
                act.triggered.connect(lambda checked, path=p: self._open_recent(path))
                self.recent_menu.addAction(act)
        else:
            self.recent_menu.addAction("(No recent files)").setEnabled(False)

    def _open_recent(self, path):
        try:
            with open(path) as f: self.editor.setText(f.read())
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", f"File not found: {path}")

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
