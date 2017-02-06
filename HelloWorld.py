#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
# You will need to create another one of these if you stack
# your headers
mh = Adafruit_MotorHAT(addr=0x60)
# mh = Adafruit_MotorHAT(addr=0x61)

frontRight = mh.getMotor(3)
frontLeft = mh.getMotor(4)
rearRight = mh.getMotor(2)
rearLeft = mh.getMotor(1)


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


def moveFoward():
    frontRight.run(Adafruit_MotorHAT.FORWARD)
    frontLeft.run(Adafruit_MotorHAT.FORWARD)
    rearRight.run(Adafruit_MotorHAT.FORWARD)
    rearLeft.run(Adafruit_MotorHAT.FORWARD)


def moveBackward():
    frontRight.run(Adafruit_MotorHAT.BACKWARD)
    frontLeft.run(Adafruit_MotorHAT.BACKWARD)
    rearRight.run(Adafruit_MotorHAT.BACKWARD)
    rearLeft.run(Adafruit_MotorHAT.BACKWARD)


def release():
    frontRight.run(Adafruit_MotorHAT.RELEASE)
    frontLeft.run(Adafruit_MotorHAT.RELEASE)
    rearRight.run(Adafruit_MotorHAT.RELEASE)
    rearLeft.run(Adafruit_MotorHAT.RELEASE)


def setMotorSpeed(speed):
    frontRight.setSpeed(speed)
    frontLeft.setSpeed(speed)
    rearRight.setSpeed(speed)
    rearLeft.setSpeed(speed)


def run():
    setMotorSpeed(110)
    # rearRight.run(Adafruit_MotorHAT.FORWARD)
    # time.sleep(2)
    # rearRight.run(Adafruit_MotorHAT.RELEASE)
    print "Forward"
    moveFoward()
    time.sleep(2)
    release()
    time.sleep(2)

    print "Backward"
    moveBackward()
    time.sleep(2)
    release()
    time.sleep(2)

run()

atexit.register(turnOffMotors)
