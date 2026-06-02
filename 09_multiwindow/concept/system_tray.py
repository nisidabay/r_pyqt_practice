#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Tray"); self.resize(300, 200)
        self.setCentralWidget(QLabel("Close the window — app stays in tray.\nRight-click tray icon to quit."))
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))
        menu = QMenu()
        show_act = menu.addAction("Show")
        show_act.triggered.connect(self.show)
        quit_act = menu.addAction("Quit")
        quit_act.triggered.connect(app.quit)
        self.tray.setContextMenu(menu)
        self.tray.show()
        self.tray.activated.connect(lambda reason: self.show() if reason == QSystemTrayIcon.ActivationReason.DoubleClick else None)
    def closeEvent(self, event):
        self.hide(); self.tray.showMessage("App", "Minimized to tray", QSystemTrayIcon.MessageIcon.Information, 2000)
        event.ignore()

app = QApplication(sys.argv); app.setQuitOnLastWindowClosed(False)
w = MainWindow(); w.show(); sys.exit(app.exec())
