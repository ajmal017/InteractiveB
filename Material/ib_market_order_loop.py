# -*- coding: utf-8 -*-
"""
IBAPI - placing limit order and storing order id

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""


from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time


class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def error(self, reqId, errorCode, errorString):
        print("Code {} {} {}".format(reqId,errorCode,errorString))
        
    def nextValidId(self, orderId):
        super().nextValidId(orderId)
        self.nextValidOrderId = orderId
        print("NextValidId:", orderId)


def websocket_con():
    app.run()


#creating object of the Contract class - will be used as a parameter for other function calls
def usTechStk(symbol,sec_type="STK",currency="USD",exchange="ISLAND"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    return contract


def usStk(symbol, sec_type='STK',currency='USD',primary_exch='SMART'):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.primaryExchange = primary_exch
    contract.exchange = 'SMART'
    return contract


#creating object of the limit order class - will be used as a parameter for other function calls
def limitOrder(direction,quantity,lmt_price):
    order = Order()
    order.action = direction
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = lmt_price
    return order


def marketOrder(direction, quantity):
    order = Order()
    order.action = direction
    order.orderType = "MKT"
    order.totalQuantity = quantity
    return order


app = TradingApp()


ticker = input("Enter a ticker: ").upper()
signal = 'BUY'
qty = 1
if ticker!="":
    qty = int(input("Enter quantity: "))
    signal = input("Buy/Sell: ").upper()

while ticker!="":
    app.connect("127.0.0.1", 7497, clientId=9999)

    # starting a separate daemon thread to execute the websocket connection
    con_thread = threading.Thread(target=websocket_con, daemon=True)
    con_thread.start()
    time.sleep(1) # some latency added to ensure that the connection is established

    order_id = app.nextValidOrderId
    app.placeOrder(order_id, usStk(ticker), marketOrder(signal, qty)) # EClient function to request contract details
    time.sleep(2) # some latency added to ensure that the contract details request has been processed
    app.disconnect()
    print("_"*30)
    print(">> Press Enter to Exit...")
    print("_" * 30)
    ticker = input("Enter a ticker: ").upper()
    if ticker != "":
        qty = int(input("Enter quantity: "))
        signal = input("Buy/Sell: ").upper()
