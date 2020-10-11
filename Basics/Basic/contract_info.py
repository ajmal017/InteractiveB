from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ids import next_reqId
import threading, time


"""
RESET THE REQUEST ID IN TWS TO START MAKING THE CALLS FROM 0
"""


class App(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error", reqId, errorCode, errorString)

    def contractDetails(self, reqId, contractDetails):
        print("Contract Details", reqId, contractDetails)


def socket_con():
    app.run()
    print("App Running")


app = App()
app.connect("127.0.0.1", 7497, 999)

thread = threading.Thread(target=socket_con,daemon=True)
thread.start()
# # GIVING TIME TO START THE THREAD
time.sleep(3)
ticker = input("Enter a stock ticker: ").upper()

contract = Contract()
contract.symbol = ticker
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"
# contract.secType = "NEWS"
# contract.exchange = "BRFG"

app.reqContractDetails(reqId=next_reqId, contract=contract)
print("Contract requested")
time.sleep(5)
app.disconnect()
