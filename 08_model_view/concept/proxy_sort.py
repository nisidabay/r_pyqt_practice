#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSortFilterProxyModel, QStringListModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sort/Filter"); self.resize(400, 300)
        data = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Henry"]
        self.model = QStringListModel(data)
        self.proxy = QSortFilterProxyModel()
        self.proxy.setSourceModel(self.model)
        self.proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        lv = QListView(); lv.setModel(self.proxy)
        search = QLineEdit()
        search.setPlaceholderText("Filter...")
        search.textChanged.connect(self.proxy.setFilterFixedString)
        layout = QVBoxLayout(); layout.addWidget(search); layout.addWidget(lv)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
