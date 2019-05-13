
############### import libraries/packages ###############
from datetime import date, datetime
import datetime
from nsepy import get_history
import csv

############### fetch DateTime ###############
currentDT = datetime.datetime.now()

############### fetchData ###############
# symbolCode = input("enter the symbol code")
symbolCode = 'dmart'

stockData = get_history(symbol=symbolCode, start=date(2019,3,1), end=date(currentDT.year,currentDT.month,currentDT.day))

# print(stockData.columns)
fetchData = stockData.tail()
# print(stockData['Open'])
print(fetchData)
# stockData[['Close']].plot()

############### store historicla data into csv file ###############
prefix = 'dataOf_'
stockSymbol = stockData
suffix = '.csv'
fileName = prefix+symbolCode+suffix
# print(fileName)

with open(fileName, "w") as cFile:
    for row in fetchData:
        print(row)
        stockWriter = csv.writer(cFile)
        # stockWriter.writerow(stockData.columns)
        stockWriter.writerows(row)
cFile.close()
