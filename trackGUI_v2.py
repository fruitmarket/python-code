# Raspberry & Arduino setup
from nanpy import (ArduinoApi, SerialManager)
from time import sleep
from datetime import datetime

# GUI import
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QTime, QTimer

# Video camera import
import cv2
import threading
import queue

running = False
capture_thread = None
q = queue.Queue()

# Arduino pin setup
try:
    connectMain = SerialManager(device='/dev/ttyACM1')
    m = ArduinoApi(connection=connectMain)
except:
    print("Main connection failed!")

try:
    connectLaser = SerialManager(device='/dev/ttyACM2')
    laser = ArduinoApi(connection=connectLaser)
except:
    print("Laser connection failed!")


# Parameter setup
valveDelay = 70  # unit: (msec)
sensor = [2, 3, 4, 5, 6, 7, 8, 9]
rewardPort = ['A0', 'A1', 'A2', 'A3']
idx_sensor = 1
idValve = 1
state = 1
trial_current = 0
state_valve1 = state_valve2 = state_valve3 = state_valve4 = False

for index in range(0, 8):
    m.pinMode(sensor[index], m.INPUT)
for index in range(0, 4):
    m.pinMode(rewardPort[index], m.OUTPUT)


def valve_open(index_valve):
    m.digitalWrite(rewardPort[index_valve], m.HIGH)
    sleep(valveDelay/1000)
    m.digitalWrite(rewardPort[index_valve], m.LOW)


def trigger_laser(time_pulseon, time_pulseoff):
    laser.digitalWrite('A0', laser.HIGH)
    sleep(time_pulseon)
    laser.digitalWrite('A0', laser.LOW)
    sleep(time_pulseoff)


def print_sensor(index_sensor):
    time_epoch = datetime.utcnow()
    print(time_epoch, '\t', index_sensor, '\n')


def print_valve(id_valve):
    time_epoch = datetime.utcnow()
    print(time_epoch, '\t', id_valve, '\n')


def read_sensor():
    """
    #################  Read sensor  ##################
    """
    [tmp_out, mod_out, quot_out] = 0
    tmp_out = 0
    mod_out = 0
    qout_out = 0
    global idx_sensor, trial_current, state_valve1, state_valve2, state_valve3, state_valve4

    while True:
        sleep(0.001)
        tmp_out = m.digitalRead(sensor[idx_sensor])
        if tmp_out == 1:
            print_sensor(idx_sensor)
            mod_out = idx_sensor % 2
            quot_out = idx_sensor / 2
            idx_sensor = idx_sensor + 1
            if idx_sensor == 2 & state_valve1:
                index_valve = 1
                valve_open(index_valve)

            if idx_sensor == 4 & state_valve2:
                index_valve = 2
                valve_open(index_valve)

            if idx_sensor == 6 & state_valve3:
                index_valve = 3
                valve_open(index_valve)

            if idx_sensor == 8 & state_valve4:
                index_valve = 4
                valve_open(index_valve)

            if idx_sensor == 8:
                idx_sensor = 0
                trial_current = trial_current + 1
            break
        return trial_current, idx_sensor

'''
##############################################################
###################  Web cam importing  ######################
##############################################################
'''


def grab(cam, queue, width, height, fps):
    global running
    capture = cv2.VideoCapture(cam)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    capture.set(cv2.CAP_PROP_FPS, fps)

    while (running):
        frame = {}
        capture.grab()
        retval, img = capture.retrieve(0)
        frame["img"] = img

        if queue.qsize() < 10:
            queue.put(frame)
        else:
            print
            queue.qsize()


class OwnImageWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(OwnImageWidget, self).__init__(parent)
        self.image = None

    def setImage(self, image):
        self.image = image
        sz = image.size()
        self.setMinimumSize(sz)
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QtCore.QPoint(0, 0), self.image)
        qp.end()


'''
##############################################################
###################  GUI import libraries  ###################
##############################################################
'''
# load ui file
# my_uifile = 'trackGUI.ui'
my_uifile = 'C:\\Users\\Jun\\Desktop\\pyqt5.trackGUI.ui'
form_1, base_1 = uic.loadUiType(my_uifile)


class MyTrackGui(base_1, form_1):
    def __init__(self):
        super(base_1, self).__init__()
        state_valve1 = False
        state_valve2 = False
        state_valve3 = False
        state_valve4 = False
        self.setupUi(self)
        self.task_start.clicked.connect(self.clicked_task_start)
        self.task_stop.clicked.connect(self.clicked_task_stop)
        self.trial_total.setText('90')
        # Connect valves
        self.valve1.clicked.connect(self.clicked_valve1)
        self.valve2.clicked.connect(self.clicked_valve2)
        self.valve3.clicked.connect(self.clicked_valve3)
        self.valve4.clicked.connect(self.clicked_valve4)
        # self.valve2.setChecked(True)
        # self.valve4.setChecked(True)
        # Connect clock
        self.task_timer.setNumDigits(6)
        self.currentTime = QTime(0, 0, 0)
        self.task_timer.display(self.currentTime.toString("mm:ss"))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.clock_tick)
        # Connect laser state
        self.laser_state.setText(str('OFF'))
    # Video
        self.timer_video = QTimer(self)
        self.timer_video.timeout.connect(self.update_frame)
        self.window_video = OwnImageWidget(self.window_video)
        self.window_width = self.window_video.frameSize().width()
        self.window_height = self.window_video.frameSize().height()

    def clock_tick(self):
        self.currentTime = self.currentTime.addSecs(1)
        self.task_timer.display(self.currentTime.toString('mm:ss'))

    def update_frame(self):
        if not q.empty():
            frame = q.get()
            img = frame["img"]
            img_height, img_width, img_colors = img.shape
            # scale_w = float(self.window_width) / float(img_width)
            # scale_h = float(self.window_height) / float(img_height)
            scale_w = 240 / float(img_width)
            scale_h = 141 / float(img_height)
            scale = min([scale_w, scale_h])
            if scale == 0:
                scale = 1
            img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, bpc = img.shape
            bpl = bpc * width
            image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)
            self.window_video.setImage(image)

    def clicked_task_start(self):
        global state, trial_current, idx_sensor, running
        # video
        running = True
        capture_thread.start()
        self.timer_video.start(1)
        # clock
        self.timer_clock.start(1000)
        # maze parameters
        trial_total = float(self.trial_total.text())
        time_high = float(self.laser_hightime.text())
        time_low = float(self.laser_lowtime.text())
        sensor_on = float(self.laser_on.text())
        sensor_off = float(self.laser_off.text())
        self.laser_state.setText(str('IDLE'))

# main arduino code
        if state:
            read_sensor()
            if 30 <= trial_current < 60:
                while True:
                    self.laser_state.setText(str('ON'))
                    if sensor_on <= idx_sensor <= sensor_off:
                        trigger_laser(time_high, time_low)
                    break

            if trial_current == trial_total:
                state = 0
            self.task_stop.clicked.connect(self.clicked_task_stop)

    def clicked_task_stop(self):
        global state
        state = 0
        self.timer_clock.stop()
        self.timer_video.stop()
        return state

    def clicked_valve1(self):
        global state_valve1
        state_valve1 = True
        return state_valve1

    def clicked_valve2(self):
        global state_valve2
        state_valve2 = True
        return state_valve2

    def clicked_valve3(self):
        global state_valve3
        state_valve3 = True
        return state_valve3

    def clicked_valve4(self):
        global state_valve4
        state_valve4 = True
        return state_valve4


if __name__ == '__main__':
    capture_thread = threading.Thread(target=grab, args=(0, q, 1280, 720, 15))
    app = QApplication(sys.argv)
    ex = MyTrackGui()
    ex.show()
    sys.exit(app.exec_())