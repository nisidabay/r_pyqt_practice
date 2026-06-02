#!/usr/bin/env python3
"""Task Timer — Main window + popup timer, system tray minimize."""
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QTimer as QtTimer, QSettings, pyqtSignal, QObject
from PyQt6.QtGui import QPalette, QColor

class TimerWindow(QMainWindow):
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Timer"); self.setFixedSize(280, 180)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        self.remaining = 0
        self.display = QLCDNumber(); self.display.setDigitCount(5)
        self.display.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.display.display("00:00")

        self.label = QLabel("Set timer duration:")
        self.spin = QSpinBox(); self.spin.setRange(1, 60); self.spin.setValue(5)
        self.spin.setSuffix(" min")

        start_btn = QPushButton("Start"); start_btn.clicked.connect(self._start)
        cancel_btn = QPushButton("Cancel"); cancel_btn.clicked.connect(self.close)

        btn_row = QHBoxLayout()
        btn_row.addWidget(start_btn); btn_row.addWidget(cancel_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.display); layout.addWidget(self.label)
        layout.addWidget(self.spin); layout.addLayout(btn_row)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

        self.timer = QtTimer()
        self.timer.timeout.connect(self._tick)

    def _start(self):
        self.remaining = self.spin.value() * 60
        self.spin.setEnabled(False)
        self._update_display()
        self.timer.start(1000)

    def _tick(self):
        self.remaining -= 1
        self._update_display()
        if self.remaining <= 0:
            self.timer.stop()
            self.display.display("DONE!")
            QMessageBox.information(self, "Timer", "Time's up!")
            self.finished.emit()

    def _update_display(self):
        m, s = divmod(self.remaining, 60)
        self.display.display(f"{m:02d}:{s:02d}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Timer"); self.resize(350, 200)

        status = QLabel("No active timer")
        self.timer_btn = QPushButton("New Timer...")
        self.timer_btn.clicked.connect(self._new_timer)

        layout = QVBoxLayout()
        layout.addWidget(status); layout.addWidget(self.timer_btn)
        c = QWidget(); c.setLayout(layout); self.setCentralWidget(c)

        # System tray
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        menu = QMenu()
        menu.addAction("Show", self.show)
        menu.addAction("New Timer", self._new_timer)
        menu.addSeparator()
        menu.addAction("Quit", app.quit)
        self.tray.setContextMenu(menu)
        self.tray.show()

    def closeEvent(self, event):
        self.hide()
        self.tray.showMessage("Task Timer", "Minimized to tray", QSystemTrayIcon.MessageIcon.Information, 2000)
        event.ignore()

    def _new_timer(self):
        self.timer_window = TimerWindow()
        self.timer_window.finished.connect(lambda: self.setWindowTitle("Task Timer — Finished!"))
        self.timer_window.finished.connect(lambda: self.tray.showMessage("Task Timer", "Timer finished!", QSystemTrayIcon.MessageIcon.Information, 3000))
        self.timer_window.show()

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
w = MainWindow(); w.show(); sys.exit(app.exec())
