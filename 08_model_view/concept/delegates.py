#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtGui import QColor

class ColorDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        if index.column() == 1 and index.data():
            val = int(index.data())
            if val > 90: option.backgroundBrush = QColor(76, 175, 80, 100)
            elif val < 70: option.backgroundBrush = QColor(244, 67, 54, 100)

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__(); self._data = data
    def rowCount(self, p=None): return len(self._data)
    def columnCount(self, p=None): return 2
    def data(self, idx, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return list(self._data[idx.row()].values())[idx.column()]
    def headerData(self, s, o, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole: return ["Name", "Score"][s]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delegate Colors"); self.resize(350, 250)
        data = [{"name": "Alice", "score": "95"}, {"name": "Bob", "score": "60"},
                {"name": "Carol", "score": "85"}, {"name": "Dave", "score": "72"}]
        tv = QTableView(); tv.setModel(TableModel(data))
        tv.setItemDelegateForColumn(1, ColorDelegate(self))
        self.setCentralWidget(tv)

app = QApplication(sys.argv); w = MainWindow(); w.show(); sys.exit(app.exec())
