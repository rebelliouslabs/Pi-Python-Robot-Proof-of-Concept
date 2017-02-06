#from RobotRuntime import RobotRuntime
from PiBot import PiBot
import time
#robot = RobotRuntime()
#robot.run()

print "Rotate Left"
bot = PiBot()
bot.rotateLeft()
time.sleep(3)
bot.release()
time.sleep(1)
print "Rotate RIght"
bot.rotateRight()
time.sleep(3)
bot.release()
time.sleep(1)
print "Move Forward"
bot.moveForward()
time.sleep(3)
bot.release()
time.sleep(1)
print "Move Backward"
bot.moveBackward()
time.sleep(3)
bot.release()

print "Done"