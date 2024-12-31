import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from datetime import datetime
plt.style.use('classic')
import yfinance as yf
from currency_converter import CurrencyConverter
import seaborn as sns

def convert(a):
    c = CurrencyConverter()
    f_cu = 'USD'
    to_cu = 'INR'
    con = c.convert(a, f_cu, to_cu)
    return con
today = datetime.now().date().strftime("%Y-%m-%d")
n=int(input("Enter the number of stocks you want to compare"))
symbol=[]
while True:
    for i in range(n):
        arr = input("Enter your Ticker: ")
        symbol.append(arr)

#stinfo=yf.Ticker(symbol)
#stinfo=symbol.info
# for key,values in stinfo.items():
#     print(key,":",values)
# b=symbol.major_holders
# a=symbol.institutional_holders

    # d = symbol.dividends
    # data = d.resample('Y').sum()
    # data = data.reset_index()
    # data['Year'] = data['Date'].dt.year
    # div=convert(d)
    price=[]
    df_prices = pd.DataFrame(columns=['Stock Symbol', 'Current Price (INR)'])
    df_list=[]
    for i in symbol:
        data= yf.Ticker(i).info
        cntprice = data['currentPrice']
        print(f"Current price of the {i} is INR: {convert(cntprice)}")

        # price.append(cntprice)
        # print(price)
        df_symbol = pd.DataFrame({'Stock Symbol': [i], 'Current Price (INR)': [convert(cntprice)]})
        df_list.append(df_symbol)
    df_prices = pd.concat(df_list, ignore_index=True)

    datah = df_prices.pivot(index="Stock Symbol", columns="Current Price (INR)", values="Current Price (INR)")
    plt.figure(figsize=(10, 6))
    sns.heatmap(datah, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    plt.title('Current Prices of Stocks (Heatmap)')
    plt.show()


        # print(symbol.info['freeCashflow'])
        # p=symbol.history(start="2000-01-01",end=today) #we can add 1m or 1y or 1d or start=2000-01-01,end=2003-01-01

##########################################################################################



# Pivot the DataFrame for heatmap


# Plotting the heatmap

######################################################
 #    plt.figure()
 #    plt.plot(p['Close'])
 #    plt.show()
 # ###############################################################################
    # plt.figure()
    # plt.bar(data['Year'], data['Dividends'])
    # plt.ylabel('Dividend Yield ($)')
    # plt.xlabel('Year')
    # plt.title(f'{symbol} Dividends History')
    # plt.xlim(2000, 2023)
    # plt.show()
    #
#################################################################################
#next tasks

#getting live data from market
