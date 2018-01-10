# GUI import
import sys
from PyQt5.QtWidgets import QApplication, QLCDNumber
from PyQt5 import uic, QtCore
from PyQt5.QtCore import QTime, QTimer

class Clock(QLCDNumber):

    def __init__(self, digits=8, parent=None):
        super(Clock, self).__init__(digits, parent)
        self.setWindowTitle("Digital Clock")
        # Timer
        self.currentTime = QTimer()
        # Connect timer
        self.currentTime.timeout.connect(self._update)
        # Start
        self.currentTime.start(0)

    def _update(self):
        """Update display each one second"""
        time = QTime.currentTime().toString()
        self.display(time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Clock()
    ex.show()
    sys.exit(app.exec_())