import requests
r = requests.get('https://alphavantage.com/query?function=BATCH_STOCK_QUOTES&symbols=PRED&apikey=QTNISIBHR5PBVIHR')
predprice = r["price"]
print predprice
