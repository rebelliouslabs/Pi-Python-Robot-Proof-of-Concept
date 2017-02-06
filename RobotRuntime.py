from websocket_server import WebsocketServer

class RobotRuntime:

    def __init__(self, RobotWSHandler):
        # Set Up Web Sockets
        self.webSocketHandler = WebSocketHandler
        self.registerWebSocket()

    def registerWebSocket(self):
        if(self.webSocketHandler):
            self.server = SimpleWebSocketServer('', 8081, self.webSocketHandler)


    def run(self):
        if(self.server):
            self.server.serveforever()