#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QAbstractTableModel, Qt

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__(); self._data = data
    def rowCount(self, parent=None): return len(self._data)
    def columnCount(self, parent=None): return 2
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            row = self._data[index.row()]
            return row["name"] if index.column() == 0 else str(row["score"])
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return ["Name", "Score"][section]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom TableModel"); self.resize(350, 250)
        data = [{"name": "Alice", "score": 95}, {"name": "Bob", "score": 87}]
        tv = QTableView(); tv.setModel(TableModel(data))
        self.setCentralWidget(tv)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
