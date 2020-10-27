from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ids import next_reqId
import threading, time
import json

"""
RESET THE REQUEST ID IN TWS TO START MAKING THE CALLS FROM 0
"""


class App(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    # def error(self, reqId, errorCode, errorString):
    #     print("Error", reqId, errorCode, errorString)

    def contractDetails(c, reqId, contractDetails):
        print("Contract Details", reqId, contractDetails)

        with open(f"{ticker}.json", 'w') as file:
            c = contractDetails
            # print(c)
            con_details = {
            "ConId": c.contract.conId,
            "SecId": c.contract.secId,
            "marketName":c.marketName,
            "minTick": c.minTick,
            "orderTypes": c.orderTypes,
            "validExchanges": c.validExchanges,
            "priceMagnifier": c.priceMagnifier,
            "underConId": c.underConId,
            "longName": c.longName,
            "contractMonth": c.contractMonth,
            "industry": c.industry,
            "category": c.category,
            "subcategory": c.subcategory,
            "timeZoneId": c.timeZoneId,
            'tradingHours': c.tradingHours,
            'liquidHours': c.liquidHours,
            'evRule': c.evRule,
            'evMultiplier': c.evMultiplier,
            'mdSizeMultiplier': c.mdSizeMultiplier,
            'aggGroup': c.aggGroup,
            'underSymbol': c.underSymbol,
            'underSecType': c.underSecType,
            'marketRuleIds': c.marketRuleIds,
            'secIdList': c.secIdList,
            'realExpirationDate': c.realExpirationDate,
            'lastTradeTime': c.lastTradeTime,
            'cusip': c.cusip,
            'ratings': c.ratings,
            'descAppend': c.descAppend,
            'bondType': c.bondType,
            'couponType': c.couponType,
            'callable': c.callable,
            'putable': c.putable,
            'coupon': c.coupon,
            'convertible': c.convertible,
            'maturity': c.maturity,
            'issueDate': c.issueDate,
            'nextOptionDate': c.nextOptionDate,
            'nextOptionType': c.nextOptionType,
            'nextOptionPartial': c.nextOptionPartial,
            'notes': c.notes}
            file.write(json.dumps(con_details))
            file.close()
        # print(contractDetails.__init__().contract)
        print("*"*30)
        for i in con_details:
            print(i,":",con_details[i])


def socket_con():
    app.run()


app = App()

ticker = input("Enter a stock ticker: ").upper()
while ticker!="":
    app.connect("127.0.0.1", 7497, 999)
    thread = threading.Thread(target=socket_con,daemon=True)
    thread.start()
    # # GIVING TIME TO START THE THREAD
    time.sleep(2)

    contract = Contract()
    contract.symbol = ticker
    contract.secType = "STK"
    contract.currency = "USD"
    contract.exchange = "SMART"
    # contract.secType = "NEWS"
    # contract.exchange = "BRFG"

    print("Contract requested")
    data = app.reqContractDetails(reqId=next_reqId, contract=contract)
    time.sleep(5)
    print("Data:",data)
    time.sleep(2)
    app.disconnect()
    time.sleep(2)

    ticker = input("Enter a stock ticker: ").upper()
