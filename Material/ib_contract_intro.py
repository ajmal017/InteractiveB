# -*- coding: utf-8 -*-
"""
IBAPI - Getting Contract info

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ids import next_reqId
import time


class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def error(self, reqId, errorCode, errorString):
        print("Error {} {} {}".format(reqId,errorCode,errorString))
        
    def contractDetails(self, reqId, contractDetails):
        print("redID: {}, contract:{}".format(reqId,contractDetails))

    

app = TradingApp()
ticker = input("Enter a stock ticker: ").upper()

while ticker!="":

    app.connect("127.0.0.1", 4002, clientId=0)
    contract = Contract()
    contract.symbol = ticker
    contract.secType = "STK"
    contract.currency = "USD"
    contract.exchange = "SMART"

    app.reqContractDetails(next_reqId, contract)
    time.sleep(3)
    app.run()
    time.sleep(2)
    app.disconnect()
    ticker = input("Enter a stock ticker: ").upper()
