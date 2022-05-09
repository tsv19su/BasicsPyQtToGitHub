import PyQt5
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
import sys


class MWidget(QWidget):
    def __init__(self):
        super(MWidget, self).__init__()
        self.setWindowTitle('Simple')
        self.btn = QPushButton('Start/Stop', self)
        self.btn.setGeometry(10, 10, 150, 50)
        self.btn.clicked.connect(self.on_btn_click)
        self.progress = QProgressBar(self)
        self.progress.setRange(0, 100)
        self.progress.setGeometry(10, 100, 200, 20)
        self.timer = QTimer(self)
        self._n = 0

    def on_btn_click(self):
        if self.timer.isActive():
            self.timer.stop()
            self.timer.disconnect()
        else:
            self.timer.setInterval(300)
            self.timer.timeout.connect(self.do_progress)
            self.timer.start()

    def do_progress(self):
        self._n += 1
        self.progress.setValue(self._n)
        if self._n == 100:
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MWidget()
    w.show()
    sys.exit(app.exec_())
