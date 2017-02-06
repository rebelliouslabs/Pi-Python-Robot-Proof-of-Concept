#from RobotRuntime import RobotRuntime
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import PiBot
import time
#robot = RobotRuntime()
#robot.run()

mh = Adafruit_MotorHAT(addr=0x60)

bot = PiBot(mh)
bot.rotateLeft()
time.sleep(3)
bot.release()
time.sleep(1)

bot.rotateRight()
time.sleep(3)
bot.release()
time.sleep(1)

bot.moveForward()
time.sleep(3)
bot.release()
time.sleep(1)

bot.moveBackward()
time.sleep(3)
bot.release()

print "Done"