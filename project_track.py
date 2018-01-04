##################################################
#########  Raspberry - Arduino setup  ############
##################################################
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

# Make connection
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

##################################################
##############  Main arduino code  ###############
##################################################

valveDelay = 70
reward = False

sensor = [2, 3, 4, 5, 6, 7, 8, 9]
rewardPort = ['A0', 'A1', 'A2', 'A3']
idSensor = 0
isValve = 0
state = 1 # 0: idle, 1: task
nTrial = 0
totalTrial = 90

for index in range(0, 8):
    m.pinMode(sensor[index], m.INPUT)
for index in range(0, 4):
    m.pinMode(rewardPort[index], m.OUTPUT)

def readSensor():
    tmp_out = 0
    mod_out = 0
    qout_out = 0

    sleep(0.001)

# pinMode Setup



# pinMode
ledPin = 7
buttonPin = 8
ledState = False
buttonState = 0

# Setup the pinModes
m.pinMode(ledPin, m.OUTPUT)
m.pinMode(buttonPin, m.INPUT)

# Main
try:
    while True:
        buttonState = m.digitalRead(buttonPin)
        print("Our button state is: {}".format(buttonState))
        if buttonState:
            if ledState:
                m.digitalWrite(ledPin,m.LOW)
                ledState = False
                print("LED OFF")
                sleep(1)
            else:
                m.digitalWrite(ledPin,m.HIGH)
                ledState = True
                print("LED ON")
                sleep(1)
except:
    m.digitalWrite(ledPin,m.LOW)