# Model/View — Data-Driven Widgets

Tables, trees, and lists backed by data models — the Qt model/view architecture.

## Quick Start

```bash
python3 table_widget.py       # QTableWidget — simple row/col table
python3 table_editable.py     # Editable cells with itemChanged signal
python3 tree_widget.py        # QTreeWidget — hierarchical data
python3 list_view.py          # QListView + QStringListModel — model/view separation
python3 table_model.py        # QAbstractTableModel — custom data source
python3 tree_model.py         # QStandardItemModel — programmatic tree
python3 proxy_sort.py         # QSortFilterProxyModel — filter and sort
python3 delegates.py          # Custom cell rendering with QStyledItemDelegate
```

## Learning Path

| File | Concept |
|------|---------|
| `table_widget.py` | QTableWidget, setItem, headers, itemClicked |
| `table_editable.py` | itemChanged signal, bidirectional data sync |
| `tree_widget.py` | QTreeWidgetItem, parent-child hierarchy |
| `list_view.py` | Model/view separation, one model → two views |
| `table_model.py` | QAbstractTableModel subclass, data() + rowCount() |
| `tree_model.py` | QStandardItemModel + QTreeView |
| `proxy_sort.py` | QSortFilterProxyModel, real-time filtering |
| `delegates.py` | QStyledItemDelegate, custom background colors |

## Common Patterns

```python
# Populate table
table = QTableWidget(rows, cols)
table.setHorizontalHeaderLabels(["Name", "Score"])
table.setItem(row, col, QTableWidgetItem("value"))

# Custom model
class MyModel(QAbstractTableModel):
    def rowCount(self, parent): return len(self._data)
    def columnCount(self, parent): return 2
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

# Filter proxy
proxy = QSortFilterProxyModel()
proxy.setSourceModel(model)
proxy.setFilterFixedString("search term")
```

## Now Build Your Own

Build a contact table with columns: Name, Phone, Email. Add a search bar that filters rows in real time using QSortFilterProxyModel.
