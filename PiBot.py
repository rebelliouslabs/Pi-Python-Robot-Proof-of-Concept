from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit


class PiBot:

    def __init__(self):
        self.name = 'PiBot'

        # Register Motor Controller
        self.mh1 = Adafruit_MotorHAT(addr=0x60)

        # Register motors
        self.frontRight = self.mh1.getMotor(3)
        self.frontLeft = self.mh1.getMotor(4)
        self.rearRight = self.mh1.getMotor(2)
        self.rearLeft = self.mh1.getMotor(1)

        # Register a die command to kill motors if program crashes.
        atexit.register(self.die)

    # Move Forward
    #
    # Tells the robot to move forward
    def moveForward(self):
        self.frontRight.run(Adafruit_MotorHAT.FORWARD)
        self.frontLeft.run(Adafruit_MotorHAT.FORWARD)
        self.rearRight.run(Adafruit_MotorHAT.FORWARD)
        self.rearLeft.run(Adafruit_MotorHAT.FORWARD)

    # Move Backward
    #
    # Tells the robot to move backward
    def moveBackward(self):
        self.frontRight.run(Adafruit_MotorHAT.BACKWARD)
        self.frontLeft.run(Adafruit_MotorHAT.BACKWARD)
        self.rearRight.run(Adafruit_MotorHAT.BACKWARD)
        self.rearLeft.run(Adafruit_MotorHAT.BACKWARD)

    # Rotate left
    #
    # Rotates the robot clock-wise
    def rotateLeft(self):
        self.frontRight.run(Adafruit_MotorHAT.FORWARD)
        self.frontLeft.run(Adafruit_MotorHAT.BACKWARD)
        self.rearRight.run(Adafruit_MotorHAT.FORWARD)
        self.rearLeft.run(Adafruit_MotorHAT.BACKWARD)

    # Rotate Right
    #
    # Rotates the robot counter-clock-wise
    def rotateRight(self):
        self.frontRight.run(Adafruit_MotorHAT.BACKWARD)
        self.frontLeft.run(Adafruit_MotorHAT.FORWARD)
        self.rearRight.run(Adafruit_MotorHAT.BACKWARD)
        self.rearLeft.run(Adafruit_MotorHAT.FORWARD)

    # Release
    #
    # Release the motor
    def release(self):
        self.frontRight.run(Adafruit_MotorHAT.RELEASE)
        self.frontLeft.run(Adafruit_MotorHAT.RELEASE)
        self.rearRight.run(Adafruit_MotorHAT.RELEASE)
        self.rearLeft.run(Adafruit_MotorHAT.RELEASE)

    # Die
    #
    # Used to kill all motors of this instance if the code
    # crashes.
    def die(self):
        self.mh1.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh1.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh1.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh1.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    # Set Motor Speed
    #
    # Sets the motors should go.
    def setMotorSpeed(self, speed):
        self.frontRight.setSpeed(speed)
        self.frontLeft.setSpeed(speed)
        self.rearRight.setSpeed(speed)
        self.rearLeft.setSpeed(speed)