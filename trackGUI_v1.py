# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trackGUI_v1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(610, 420)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setKerning(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 391, 371))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.task_stop = QtWidgets.QPushButton(self.groupBox)
        self.task_stop.setGeometry(QtCore.QRect(290, 30, 91, 51))
        self.task_stop.setObjectName("task_stop")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 361, 43))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.valve1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.valve1.setObjectName("valve1")
        self.horizontalLayout.addWidget(self.valve1)
        self.valve2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.valve2.setObjectName("valve2")
        self.horizontalLayout.addWidget(self.valve2)
        self.valve3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.valve3.setObjectName("valve3")
        self.horizontalLayout.addWidget(self.valve3)
        self.valve4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.valve4.setObjectName("valve4")
        self.horizontalLayout.addWidget(self.valve4)
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 20, 141, 61))
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.mouse_id = QtWidgets.QLineEdit(self.groupBox_10)
        self.mouse_id.setObjectName("mouse_id")
        self.verticalLayout_9.addWidget(self.mouse_id)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 210, 361, 68))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_9 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.trial_total = QtWidgets.QSpinBox(self.groupBox_9)
        self.trial_total.setObjectName("trial_total")
        self.trial_total.clicked.connect(self.clicked_trial_total)
        self.verticalLayout_8.addWidget(self.trial_total)
        self.horizontalLayout_2.addWidget(self.groupBox_9)
        self.groupBox_7 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.trial_current = QtWidgets.QLCDNumber(self.groupBox_7)
        self.trial_current.setObjectName("trial_current")
        self.verticalLayout_6.addWidget(self.trial_current)
        self.horizontalLayout_2.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.trial_inblock = QtWidgets.QLCDNumber(self.groupBox_8)
        self.trial_inblock.setObjectName("trial_inblock")
        self.verticalLayout_7.addWidget(self.trial_inblock)
        self.horizontalLayout_2.addWidget(self.groupBox_8)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 290, 131, 61))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.position = QtWidgets.QLCDNumber(self.groupBox_6)
        self.position.setObjectName("position")
        self.verticalLayout_5.addWidget(self.position)
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_12.setGeometry(QtCore.QRect(180, 290, 171, 61))
        self.groupBox_12.setObjectName("groupBox_12")
        self.time_task = QtWidgets.QLCDNumber(self.groupBox_12)
        self.time_task.setGeometry(QtCore.QRect(40, 30, 111, 21))
        self.time_task.setObjectName("time_task")
        self.task_start = QtWidgets.QPushButton(self.groupBox)
        self.task_start.setGeometry(QtCore.QRect(160, 30, 101, 51))
        self.task_start.setObjectName("task_start")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(430, 10, 171, 371))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.laser_hightime = QtWidgets.QSpinBox(self.groupBox_2)
        self.laser_hightime.setObjectName("laser_hightime")
        self.verticalLayout.addWidget(self.laser_hightime)
        self.laser_hightime.clicked.connect(self.clicked_laser_hightime)
        self.verticalLayout_10.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.laser_lowtime = QtWidgets.QSpinBox(self.groupBox_3)
        self.laser_lowtime.setObjectName("laser_lowtime")
        self.verticalLayout_2.addWidget(self.laser_lowtime)
        self.verticalLayout_10.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.laser_on = QtWidgets.QSpinBox(self.groupBox_4)
        self.laser_on.setObjectName("laser_on")
        self.verticalLayout_3.addWidget(self.laser_on)
        self.verticalLayout_10.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.laser_off = QtWidgets.QSpinBox(self.groupBox_5)
        self.laser_off.setObjectName("laser_off")
        self.verticalLayout_4.addWidget(self.laser_off)
        self.verticalLayout_10.addWidget(self.groupBox_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 10, 20, 371))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Main set-up"))
        self.task_stop.setText(_translate("MainWindow", "STOP"))
        self.valve1.setText(_translate("MainWindow", "Valve1"))
        self.valve2.setText(_translate("MainWindow", "Valve2"))
        self.valve3.setText(_translate("MainWindow", "Valve3"))
        self.valve4.setText(_translate("MainWindow", "Valve4"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Mouse ID"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Total trial"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Current trial"))
        self.groupBox_8.setTitle(_translate("MainWindow", "In block trial"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Current location"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Task time"))
        self.task_start.setText(_translate("MainWindow", "START"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Laser set-up"))
        self.label_3.setText(_translate("MainWindow", "High time (ms)"))
        self.label_4.setText(_translate("MainWindow", "Low time (ms)"))
        self.label_5.setText(_translate("MainWindow", "Laser on sensor"))
        self.label_6.setText(_translate("MainWindow", "Laser off sensor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



def stop_clicked(self):
    state = 0
    return state


def start_clicked(self, total_trial):
    state = 1
    if state:
        read_sensor()
        if nTrial == total_trial:
            state = 0


def clicked_trial_total(self):
    total_trial = float(self.trial_total.txt())
    return total_trial


def clicked_laser_hightime(self):
    hightime = float(self.laser_hightime.txt())
    return hightime


def clicked_laser_lowtime(self):
    lowtime = float(self.laser_lowtime.txt())
    return lowtime


def clicked_laser_on(self):
    sensor_on = float(self.laser_on.txt())
    return sensor_on


def clicked_laser_off(self):
    sensor_off = float(self.laser_off.txt())
    return sensor_off


def clicked_valve1(self):
    valve_1 = 'A0'
    return valve_1


def clicked_valve(self):
    valve_2 = 'A1'
    return valve_2


def clicked_valve(self):
    valve_3 = 'A2'
    return valve_3


def clicked_valve(self):
    valve_4 = 'A3'
    return valve_4


"""
#########  Raspberry - Arduino setup  ############
"""
from nanpy import (ArduinoApi, SerialManager)
from time import sleep
from datetime import datetime

try:
    connectMain = SerialManager(device='/dev/ttyACM1')
    m = ArduinoApi(connection=connectMain)
except:
    print("Main connection failed!")

try:
    connectLaser = SerialManager(device='/dev/ttyACM2')
    l = ArduinoApi(connection=connectLaser)
except:
    print("Laser connection failed!")

"""
##############  Main Arduino code  ###############
"""

# totalTrial = 90
valveDelay = 70
reward = False
sensor = [2, 3, 4, 5, 6, 7, 8, 9]
rewardPort = ['A0', 'A1', 'A2', 'A3']
idSensor = 1
idValve = 1
nTrial = 0

for index in range(0, 8):
    m.pinMode(sensor[index], m.INPUT)
for index in range(0, 4):
    m.pinMode(rewardPort[index], m.OUTPUT)


def valve_open(index_valve):
    """
    #################  Valve Open  ###################
    """
    m.digitalWrite(rewardPort(index_valve, m.HIGH))
    sleep(valveDelay)
    m.digitalWrite(rewardPort(index_valve, m.LOW))
    reward = True


def print_sensor(id_sensor):
    """
    ############  Print Sensor & Valve  ##############
    """
    timeEpoch = datetime.utcnow()
    timeEpoch.second
    print(timeEpoch, '\t', id_sensor, '\n')


def print_valve(id_valve):
    timeEpoch = datetime.utcnow()
    timeEpoch.second
    print(timeEpoch, '\t', id_valve, '\n')


def read_sensor():
    """
    #################  Read sensor  ##################
    """
    [tmp_out, mod_out, quot_out] = 0
    global id_sensor
    global n_trial
    global id_valve

    while True:
        sleep(0.001)
        tmp_out = m.digitalRead(sensor(id_sensor))
        if tmp_out == 1:
            print_sensor()
            mod_out = id_sensor % 2
            quot_out = id_sensor / 2
            id_sensor = id_sensor + 1
            if mod_out == 0:
                print_valve(id_valve)
                valve_open(quot_out)
                id_valve = id_valve
            if id_sensor == 8:
                id_sensor = 0
                id_valve = 0
                n_trial = n_trial + 1
            break


def mainloop(total_trial):
    """
    #################  Main function  ##################
    """
    state = 1  # 0: idle, 1: task
    if state:
        read_sensor()
        if nTrial == total_trial:
            state = 0
