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
valveDelay = 70
reward = False
sensor = [2, 3, 4, 5, 6, 7, 8, 9]
rewardPort = ['A0', 'A1', 'A2', 'A3']
idSensor = 0
idValve = 0
nTrial = 0
totalTrial = 90

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


def read_sensor(id_sensor, n_trial):
    """
    #################  Read sensor  ##################
    """
    [tmp_out, mod_out, quot_out] = 0
    while True:
        sleep(0.001)
        tmp_out = m.digitalRead(sensor(id_sensor))
        if tmp_out == 1:
            print_sensor()
            mod_out = id_sensor % 2
            quot_out = id_sensor / 2
            id_sensor = id_sensor + 1
            if mod_out == 0:
                valve_open(quot_out)
            if id_sensor == 8:
                id_sensor = 0
                n_trial = n_trial + 1
            break


def mainloop():
    """
    #################  Main function  ##################
    """
    state = 1  # 0: idle, 1: task
    if state:
        read_sensor()
        if nTrial == totalTrial:
            state = 0