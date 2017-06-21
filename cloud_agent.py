from autobahn.twisted.websocket import WebSocketClientProtocol
from autobahn.twisted.websocket import WebSocketClientFactory

import sys
from twisted.python import log
from twisted.internet import reactor
log.startLogging(sys.stdout)

class MyClientProtocol(WebSocketClientProtocol):

   def onOpen(self):
      self.sendMessage(u"Hello, I am Jyotsna's Pi".encode('utf8'))

   def onMessage(self, payload, isBinary):
      if isBinary:
         print("Binary message received: {0} bytes".format(len(payload)))
      else:
         print("Text message received: {0}".format(payload.decode('utf8')))


if __name__ == '__main__':

   factory = WebSocketClientFactory()
   factory.protocol = MyClientProtocol

   reactor.connectTCP("192.168.100.121", 9000, factory)
   reactor.run()
