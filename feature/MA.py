# Moving Averages Code

# Load the necessary packages and modules
import pandas as pd
import matplotlib.pyplot as plt
import data.stock as st


# Simple Moving Average 
def SMA(data, ndays):
    SMA = pd.Series(data['close'].rolling(ndays).mean(), name='SMA')
    # SMA = pd.Series(pd.rolling_mean(data['close'], ndays), name='SMA')
    data = data.join(SMA)
    return data


# Exponentially-weighted Moving Average
def EWMA(data, ndays):
    EMA = pd.Series(pd.DataFrame.ewm(data['close'],
                                      span=ndays,
                                      min_periods=ndays - 1).mean(),
                                      name='EWMA_' + str(ndays))
    data = data.join(EMA)
    return data


# Retrieve the Nifty data from Yahoo finance:
XSHE000002_data = st.get_csv_data('000002.XSHE', 'price')
close = XSHE000002_data['close']

# Compute the 50-day SMA for NIFTY
n = 50
SMA_NIFTY = SMA(XSHE000002_data, n)
SMA_NIFTY = SMA_NIFTY.dropna()
SMA = SMA_NIFTY['SMA']


def get_sma(stock_code, ndays):
    stock_data = st.get_csv_data(stock_code, 'price')
    merged_data = SMA(stock_data, ndays)
    merged_data = merged_data.dropna()
    return merged_data['SMA']

# Compute the 200-day EWMA for NIFTY
ew = 200
EWMA_NIFTY = EWMA(XSHE000002_data, ew)
EWMA_NIFTY = EWMA_NIFTY.dropna()
EWMA = EWMA_NIFTY['EWMA_200']

# Plotting the NIFTY Price Series chart and Moving Averages below
plt.figure(figsize=(9, 5))
plt.plot(XSHE000002_data['close'], lw=1, label='NSE Prices')
plt.plot(SMA, 'g', lw=1, label='50-day SMA (green)')
plt.plot(EWMA, 'r', lw=1, label='200-day EWMA (red)')
plt.legend(loc=2, prop={'size': 11})
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()
