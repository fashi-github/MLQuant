# Load the necessary packages and modules
import pandas as pd
import data.stock as st
import matplotlib.pyplot as plt


# Commodity Channel Index
def CCI(data, ndays):
    TP = (data['high'] + data['low'] + data['close']) / 3
    # CCI = pd.Series((TP - pd.rolling_mean(TP, ndays)) / (0.015 * pd.rolling_std(TP, ndays)),
    CCI = pd.Series((TP - TP.rolling(ndays).mean()) / (0.015 * TP.rolling(ndays).std()),
                    name='CCI')
    data = data.join(CCI)
    return data


def get_cci(stock_code, ndays):
    stock_data = st.get_csv_data(stock_code, 'price')
    merged_data = CCI(stock_data, ndays)
    return merged_data[['date', 'CCI']]


# XSHE000002_data = st.get_csv_data('000002.XSHE', 'price')
#
# # Compute the Commodity Channel Index(CCI) for NIFTY based on the 20-day Moving average
# n = 20
# NIFTY_CCI = CCI(XSHE000002_data, n)
# CCI = NIFTY_CCI['CCI']
#
# # Plotting the Price Series chart and the Commodity Channel index below
# fig = plt.figure(figsize=(7, 5))
# ax = fig.add_subplot(2, 1, 1)
# ax.set_xticklabels([])
# plt.plot(XSHE000002_data['close'], lw=1)
# plt.title('股票价格图表')
# plt.ylabel('Close Price')
# plt.grid(True)
# bx = fig.add_subplot(2, 1, 2)
# plt.plot(CCI, 'k', lw=0.75, linestyle='-', label='CCI')
# plt.legend(loc=2, prop={'size': 9.5})
# plt.ylabel('CCI values')
# plt.grid(True)
# plt.setp(plt.gca().get_xticklabels(), rotation=30)
# plt.show()
