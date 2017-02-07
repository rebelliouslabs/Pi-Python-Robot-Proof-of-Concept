from RobotRuntime import RobotRuntime
from RobotWSHandler import RobotWSHandler
from PiBot import PiBot
import time

bot = PiBot()
bot.setMotorSpeed(150)
handler = RobotWSHandler(bot)

robot = RobotRuntime(handler)
robot.run()

print "Done"