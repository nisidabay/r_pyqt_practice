#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QPushButton,
                              QVBoxLayout, QWidget, QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit")
        self.resize(400, 300)
        self.label = QLabel("Word count: 0")
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Type or paste text here...")
        self.editor.textChanged.connect(self._count_words)
        clear = QPushButton("Clear")
        clear.clicked.connect(self.editor.clear)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.editor)
        layout.addWidget(clear)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _count_words(self):
        text = self.editor.toPlainText()
        count = len(text.split()) if text.strip() else 0
        self.label.setText(f"Word count: {count}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
