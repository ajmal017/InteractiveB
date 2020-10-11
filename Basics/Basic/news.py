from ibapi.client import EClient
from ibapi.wrapper import EWrapper

import threading
import time


class NewsApp(EClient,EWrapper):
    def __int__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode:int, errorString:str):
        print("Error",reqId,errorCode,errorString)

    def newsProviders(self, newsProviders):
        print("News Providers: ")
        for provider in newsProviders:
            print("News Provider.", provider)

def websocket_con():
    print("Initiating Run Loop...")
    app.run()

app = NewsApp()
app.connect("127.0.0.1", 7497,999)
thread = threading.Thread(target=websocket_con, daemon=True)
thread.start()
time.sleep(1)

app.reqNewsProviders()

app.disconnect()