# Source: https://www.youtube.com/watch?v=dLMKvrmWB68
from PyQt5.QtWidgets import QApplication, QLCDNumber
from PyQt5.QtCore import QTimer, QTime


class Clock(QLCDNumber):

    def __init__(self, digits=8, parent=None):
        super(Clock, self).__init__(digits, parent)
        self.setWindowTitle("Digital Clock")
        # Timer
        self.timer = QTimer()
        # Connect timer
        self.timer.timeout.connect(self._update)
        # Start
        self.timer.start(0)

    def _update(self):
        """ Update display each one second """
        time = QTime.currentTime().toString()
        self.display(time)


if __name__ == "__main__":
    import sys
    app = QApplication([])

    w = Clock()
    w.show()
    w.resize(300, 50)

    sys.exit(app.exec_())