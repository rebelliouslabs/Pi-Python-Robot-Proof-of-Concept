from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit


class PiBot(object):

    def __init__(self):
        self.name = 'PiBot'
        print "Register Motor Contorller"
        # Register Motor Controller
        self._mh = Adafruit_MotorHAT(0x60)

        print "Register Motors"
        # Register motors
        self._frontRight = self._mh.getMotor(3)
        self._frontLeft = self._mh.getMotor(4)
        self._rearRight = self._mh.getMotor(2)
        self._rearLeft = self._mh.getMotor(1)

        # Register a die command to kill motors if program crashes.
        atexit.register(self.die)

    # Move Forward
    #
    # Tells the robot to move forward
    def moveForward(self):
        print "Moving Forward"
        self._frontRight.run(Adafruit_MotorHAT.FORWARD)
        self._frontLeft.run(Adafruit_MotorHAT.FORWARD)
        self._rearRight.run(Adafruit_MotorHAT.FORWARD)
        self._rearLeft.run(Adafruit_MotorHAT.FORWARD)

    # Move Backward
    #
    # Tells the robot to move backward
    def moveBackward(self):
        print "Moving Backward"
        self._frontRight.run(Adafruit_MotorHAT.BACKWARD)
        self._frontLeft.run(Adafruit_MotorHAT.BACKWARD)
        self._rearRight.run(Adafruit_MotorHAT.BACKWARD)
        self._rearLeft.run(Adafruit_MotorHAT.BACKWARD)

    # Rotate left
    #
    # Rotates the robot clock-wise
    def rotateLeft(self):
        print "Rotating Left"
        self._frontRight.run(Adafruit_MotorHAT.FORWARD)
        self._frontLeft.run(Adafruit_MotorHAT.BACKWARD)
        self._rearRight.run(Adafruit_MotorHAT.FORWARD)
        self._rearLeft.run(Adafruit_MotorHAT.BACKWARD)

    # Rotate Right
    #
    # Rotates the robot counter-clock-wise
    def rotateRight(self):
        print "Rotating Right"
        self._frontRight.run(Adafruit_MotorHAT.BACKWARD)
        self._frontLeft.run(Adafruit_MotorHAT.FORWARD)
        self._rearRight.run(Adafruit_MotorHAT.BACKWARD)
        self._rearLeft.run(Adafruit_MotorHAT.FORWARD)

    # Release
    #
    # Release the motor
    def release(self):
        print "Releasing"
        self._frontRight.run(Adafruit_MotorHAT.RELEASE)
        self._frontLeft.run(Adafruit_MotorHAT.RELEASE)
        self._rearRight.run(Adafruit_MotorHAT.RELEASE)
        self._rearLeft.run(Adafruit_MotorHAT.RELEASE)

    # Die
    #
    # Used to kill all motors of this instance if the code
    # crashes.
    def die(self):
        self._mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self._mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self._mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self._mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    # Set Motor Speed
    #
    # Sets the motors should go.
    def setMotorSpeed(self, speed):
        self._frontRight.setSpeed(speed)
        self._frontLeft.setSpeed(speed)
        self._rearRight.setSpeed(speed)
        self._rearLeft.setSpeed(speed)