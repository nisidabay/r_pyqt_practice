#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QToolBar, QStyle, QMessageBox)
from PyQt6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toolbar"); self.resize(500, 350)
        self.editor = QTextEdit(); self.setCentralWidget(self.editor)
        tb = self.addToolBar("Main")
        style = self.style()
        for name, slot, icon in [
            ("New", self.editor.clear, style.standardIcon(QStyle.StandardPixmap.SP_FileIcon)),
            ("About", lambda: QMessageBox.about(self, "About", "Toolbar Demo"), style.standardIcon(QStyle.StandardPixmap.SP_MessageBoxInformation))]:
            act = QAction(icon, name, self)
            act.triggered.connect(slot); tb.addAction(act)
    def _new(self): self.editor.clear()

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
