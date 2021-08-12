# Load the necessary packages and modules
import numpy as np
import pandas as pd
import data.stock as st
import matplotlib.pyplot as plt


# Ease of Movement 
def EVM(data, ndays):
    dm = ((data['high'] + data['low']) / 2) - ((data['high'].shift(1) + data['low'].shift(1)) / 2)
    br = (data['volume'] / 100000000) / (data['high'] - data['low'])
    print('br before handle:\n', br)
    br[br == np.inf] = 1
    print('br after handle:\n', br)
    EVM = dm / br
    EVM_MA = pd.Series(EVM.rolling(ndays).mean(), name='EVM')
    # EVM_MA = pd.Series(pd.rolling_mean(EVM, ndays), name = 'EVM')
    data = data.join(EVM_MA)
    return data


def get_evm(stock_code, ndays):
    stock_data = st.get_csv_data(stock_code, 'price')
    merged_data = EVM(stock_data, ndays)
    return merged_data['EVM']


get_evm('000002.XSHE', 14)

# XSHE000002_data = st.get_csv_data('000002.XSHE', 'price')
#
# # Compute the 14-day Ease of Movement for AAPL
# n = 14
# AAPL_EVM = EVM(XSHE000002_data, n)
# EVM = AAPL_EVM['EVM']
#
# # Plotting the Price Series chart and the Ease Of Movement below
# fig = plt.figure(figsize=(7, 5))
# ax = fig.add_subplot(2, 1, 1)
# ax.set_xticklabels([])
# plt.plot(XSHE000002_data['close'], lw=1)
# plt.title('AAPL Price Chart')
# plt.ylabel('Close Price')
# plt.grid(True)
# bx = fig.add_subplot(2, 1, 2)
# plt.plot(EVM, 'k', lw=0.75, linestyle='-', label='EVM(14)')
# plt.legend(loc=2, prop={'size': 9})
# plt.ylabel('EVM values')
# plt.grid(True)
# plt.setp(plt.gca().get_xticklabels(), rotation=30)
# plt.show()
