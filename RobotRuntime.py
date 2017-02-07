from websocket_server import WebsocketServer

class RobotRuntime:

    def __init__(self, RobotWSHandler):
        # Set Up Web Sockets
        self.webSocketHandler = RobotWSHandler
        self.registerWebSocket()

    def registerWebSocket(self):
        if(self.webSocketHandler):
            print "Building Service"
            self.server = WebsocketServer(8081, host='0.0.0.0')
            self.server.set_fn_message_received(self.webSocketHandler.messageReceived)


    def run(self):
        if(self.server):
            self.server.run_forever()