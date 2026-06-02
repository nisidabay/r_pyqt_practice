#!/usr/bin/env python3
import sys, json
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editable Table"); self.resize(450, 350)
        self.data = [{"Name": "Alice", "Email": "alice@e.com"},
                     {"Name": "Bob", "Email": "bob@e.com"}]
        self.table = QTableWidget(len(self.data), 2)
        self.table.setHorizontalHeaderLabels(["Name", "Email"])
        self._refresh()
        self.table.itemChanged.connect(self._on_change)
        btn = QPushButton("Show Data"); btn.clicked.connect(lambda: print(json.dumps(self.data, indent=2)))
        layout = QVBoxLayout(); layout.addWidget(self.table); layout.addWidget(btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)
    def _refresh(self):
        for r, row in enumerate(self.data):
            for c, key in enumerate(["Name", "Email"]):
                self.table.setItem(r, c, QTableWidgetItem(row[key]))
    def _on_change(self, item):
        self.data[item.row()][["Name", "Email"][item.column()]] = item.text()

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
