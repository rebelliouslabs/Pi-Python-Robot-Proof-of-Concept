from SimpleWebSocketServer import SimpleWebSocketServer

class RobotRuntime:

    def __init__(self, WebSocketHandler):
        # Set Up Web Sockets
        self.webSocketHandler = WebSocketHandler
        self.registerWebSocket()

    def registerWebSocket(self):
        if(self.webSocketHandler):
            self.server = SimpleWebSocketServer('', 8081, self.webSocketHandler)


    def run(self):
        if(self.server):
            self.server.serveforever()