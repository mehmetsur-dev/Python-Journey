# Challenge 2 Trade Logger

asset = "XAU/USD"
action = "Buy"
price = 2345.50

attention = f"TRADE ALRET: {action} position openend for {asset} at {price}"
print(attention)

print(attention. upper())

print(attention. replace("Buy", "Sell"))

print(attention. find(asset))
