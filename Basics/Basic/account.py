from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import threading, time
from ids import next_reqId


class TradeApp(EWrapper,EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def error(self, reqId, errorCode:int, errorString:str):
        print("Error:",reqId,errorCode,errorString)

    def accountSummary(self, reqId: int, account: str, tag: str, value: str,currency: str):
        print(tag,":",value)


def websocket_con():
    print("Initiating RUN loop")
    app.run()


app = TradeApp()
app.connect("127.0.0.1", 4002, 0)

thread = threading.Thread(target=websocket_con, daemon=True)
thread.start()
time.sleep(3)

print("Account Summary")
print("*"*30)
app.reqAccountSummary(next_reqId, "All", "$LEDGER:USD")
time.sleep(10)
app.cancelAccountSummary(next_reqId)
print("*"*30)


print("Closing the program")
app.disconnect()
