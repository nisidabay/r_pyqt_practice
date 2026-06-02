# Threading — Keep the UI Responsive

Long-running work in background threads. The UI stays snappy while work happens.

## Quick Start

```bash
python3 blocking_demo.py       # See what a frozen UI looks like
python3 qthread_basics.py      # QThread: signals, progress, cancel
python3 thread_progress.py     # Step-by-step progress reporting
python3 thread_queue.py        # Multiple workers from a shared queue
python3 qrunnable.py           # QThreadPool + QRunnable for one-shot tasks
```

## Learning Path

| File | Concept | Key Class |
|------|---------|-----------|
| `blocking_demo.py` | time.sleep freezes the event loop | Problem demonstration |
| `qthread_basics.py` | QThread + pyqtSignal + terminate | QThread |
| `thread_progress.py` | Incremental progress, step labels | QThread.progress |
| `thread_queue.py` | Multiple workers, signals with args | QThread + custom data |
| `qrunnable.py` | Thread pool, fire-and-forget | QRunnable + QThreadPool |

## Common Patterns

```python
# QThread worker
class Worker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)
    def run(self):
        for i in range(100):
            time.sleep(0.05)
            self.progress.emit(i)
        self.finished.emit("Done")

worker = Worker()
worker.progress.connect(bar.setValue)
worker.finished.connect(lambda msg: label.setText(msg))
worker.start()

# Cancel with terminate()
cancel_btn.clicked.connect(worker.terminate)

# QRunnable + pool
task = MyRunnable()
QThreadPool.globalInstance().start(task)
```

## Now Build Your Own

Build a file search tool: enter a directory and a search term, scan files in a background thread, show matching files in a list as they're found, with a cancel button.
