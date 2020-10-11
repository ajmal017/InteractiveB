from connection import app
from ids import next_reqId

from ibapi.contract import Contract

ticker = input("Enter a stock ticker: ").upper()

contract = Contract()
contract.symbol = ticker
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"
# contract.secType = "NEWS"
# contract.exchange = "BRFG"

print("Contract Requested")
app.reqContractDetails(reqId=next_reqId, contract=contract)
print()
# app.reqNewsProviders()
