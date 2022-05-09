import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QSystemTrayIcon, QMenu


class Progress(QWidget):
    def __init__(self):
        super(Progress, self).__init__()
        self.setWindowTitle('Progress')
        self.progress = QProgressBar(self)
        self.progress.setRange(0, 100)
        self.progress.setGeometry(10, 10, 200, 20)

    def set_progress(self, progress):
        self.progress.setValue(progress)


class MWidget(QWidget):
    def __init__(self):
        super(MWidget, self).__init__()
        self.setWindowTitle('Simple')
        self.btn = QPushButton('Start/Stop', self)
        self.btn.setGeometry(10, 10, 150, 50)
        self.btn.clicked.connect(self.on_btn_click)
        self.progress = Progress()
        self.progress.show()
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
        self.progress.set_progress(self._n)
        if self._n == 100:
            self.timer.stop()


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self):
        super(SystemTrayIcon, self).__init__()
        self.menu = QMenu(None)
        exitAction = self.menu.addAction("Exit")
        self.setContextMenu(self.menu)
        self.setIcon(QIcon("periscope.png"))
        exitAction.triggered.connect(self.exit)
        self.setVisible(True)
        self.dialog = MWidget()
        self.dialog.show()

    # А это зачем?
    def exit(self):
        sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    trayIcon = SystemTrayIcon()
    trayIcon.show()
    sys.exit(app.exec_())
