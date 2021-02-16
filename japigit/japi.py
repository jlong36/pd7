import urllib.request
import json

def getStockData(str):
  stockCode = str
  url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+stockCode+'&apikey=A7614ITBN6VMPURU'
  connection = urllib.request.urlopen(url)
  data = connection.read().decode()
  myData = json.loads(data)
  date = (myData['Meta Data']['3. Last Refreshed'])
  symbol = (myData['Meta Data']['2. Symbol'])
  mostRecent = (myData['Time Series (Daily)'][date]["4. close"])
  output = ("The current price of "+symbol+" is $"+mostRecent+".")
  return output

def writeStockData(s):
  data = s
  f = open("japi.out", "a")
  f.write(data+"\n")
  f.close()


def prompt():
  code = ""
  while code != 'quit':
    code = input("Please enter the stock's code or 'quit' stop: ")
    if code != 'quit':      
      stockPrice = getStockData(code)
      writeStockData(stockPrice)
      print(stockPrice)
    else:
      print("End Program")
      print("Stock Quotes retrieved successfully!")

prompt()

master version
