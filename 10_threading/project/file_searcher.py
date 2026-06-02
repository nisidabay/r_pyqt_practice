#!/usr/bin/env python3
"""File Searcher — Search files in a directory without freezing the UI."""
import sys, os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QThread, pyqtSignal

class SearchWorker(QThread):
    found = pyqtSignal(str)        # Emit each matching file path
    progress = pyqtSignal(int)     # Total files scanned
    finished = pyqtSignal(int)     # Total matches

    def __init__(self, directory, term):
        super().__init__()
        self._dir = directory; self._term = term.lower()

    def run(self):
        count = 0
        for root, _, files in os.walk(self._dir):
            for f in files:
                if self.isInterruptionRequested():
                    return
                path = os.path.join(root, f)
                try:
                    if self._term in f.lower():
                        self.found.emit(path); count += 1
                except OSError:
                    pass
            self.progress.emit(count)
        self.finished.emit(count)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Searcher"); self.resize(550, 420)

        dir_layout = QHBoxLayout()
        self.dir_input = QLineEdit(os.path.expanduser("~"))
        browse = QPushButton("Browse")
        browse.clicked.connect(self._browse)
        dir_layout.addWidget(QLabel("Directory:"))
        dir_layout.addWidget(self.dir_input); dir_layout.addWidget(browse)

        self.term_input = QLineEdit()
        self.term_input.setPlaceholderText("Search term (matches filename)")

        self.bar = QProgressBar(); self.bar.setVisible(False)
        self.output = QTextEdit(); self.output.setReadOnly(True)

        btn_row = QHBoxLayout()
        self.search_btn = QPushButton("Search")
        self.search_btn.clicked.connect(self._search)
        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.clicked.connect(self._cancel)
        self.cancel_btn.setEnabled(False)
        btn_row.addWidget(self.search_btn); btn_row.addWidget(self.cancel_btn)

        layout = QVBoxLayout()
        layout.addLayout(dir_layout); layout.addWidget(QLabel("Search term:"))
        layout.addWidget(self.term_input); layout.addWidget(self.bar)
        layout.addWidget(self.output); layout.addLayout(btn_row)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

    def _browse(self):
        d = QFileDialog.getExistingDirectory(self, "Choose Directory")
        if d: self.dir_input.setText(d)

    def _search(self):
        self.output.clear(); self.bar.setVisible(True); self.bar.setRange(0, 0)
        self.search_btn.setEnabled(False); self.cancel_btn.setEnabled(True)
        self.worker = SearchWorker(self.dir_input.text(), self.term_input.text())
        self.worker.found.connect(lambda p: self.output.append(p))
        self.worker.finished.connect(self._on_finished); self.worker.start()

    def _cancel(self):
        if hasattr(self, 'worker') and self.worker.isRunning():
            self.worker.requestInterruption()

    def _on_finished(self, count):
        self.bar.setVisible(False)
        self.search_btn.setEnabled(True); self.cancel_btn.setEnabled(False)
        self.output.append(f"\n--- {count} matches found ---")

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
