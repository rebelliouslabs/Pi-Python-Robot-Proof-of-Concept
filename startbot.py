#from RobotRuntime import RobotRuntime
from PiBot import PiBot
import time
#robot = RobotRuntime()
#robot.run()


bot = PiBot()
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