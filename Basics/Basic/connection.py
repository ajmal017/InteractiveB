from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import time
import threading


class App(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode, errorString):
        print("Error", reqId, errorCode, errorString)

def websocket_con():
    print("Initiating RUN loop")
    app.run()


app = App()
app.connect("127.0.0.1", 7497, 0)

thread = threading.Thread(target=websocket_con, daemon=False)
thread.start()
time.sleep(1)

print("Closing the program")
app.disconnect()