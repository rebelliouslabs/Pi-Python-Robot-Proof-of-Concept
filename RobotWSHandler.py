

class RobotWSHandler:

    def __init__(self, Robot):
        self.robot = Robot

    def messageReceived(self, client, server, message):
        print "Message Received"
        code = message
        print code
        if(code == 'forward'):
            print "forward"
            self.robot.moveForward()
        elif(code == 'backward'):
            print "backward"
            self.robot.moveBackward()
        elif(code == 'rotate-left'):
            print "rotate-left"
            self.robot.rotateLeft()
        elif(code == 'rotate-right'):
            print "rotate-right"
            self.robot.rotateRight()
        elif(code == 'release'):
            print "release"
            self.robot.release()

