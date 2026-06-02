#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QPushButton,
                              QTextEdit, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog"); self.resize(400, 300)
        self.editor = QTextEdit(); self.editor.setPlaceholderText("File content appears here...")
        open_btn = QPushButton("Open"); open_btn.clicked.connect(self._open)
        save_btn = QPushButton("Save"); save_btn.clicked.connect(self._save)
        layout = QVBoxLayout(); layout.addWidget(self.editor)
        layout.addWidget(open_btn); layout.addWidget(save_btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open", "", "Text Files (*.txt);;All Files (*)")
        if path:
            with open(path) as f: self.editor.setText(f.read())

    def _save(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save", "untitled.txt", "Text Files (*.txt)")
        if path:
            with open(path, "w") as f: f.write(self.editor.toPlainText())

app = QApplication(sys.argv); window = MainWindow(); window.show(); sys.exit(app.exec())
