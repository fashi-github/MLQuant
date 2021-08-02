# Rate of Change code

# Load the necessary packages and modules
import pandas as pd
import data.stock as st
import matplotlib.pyplot as plt


# Rate of Change (ROC)
def ROC(data, n):
    N = data['close'].diff(n)
    D = data['close'].shift(n)
    ROC = pd.Series(N / D, name='Rate of Change')
    data = data.join(ROC)
    return data


def get_roc(stock_code, ndays):
    stock_data = st.get_csv_data(stock_code, ndays)
    merge_data = ROC(stock_data, ndays)
    return merge_data['ROC']


# Retrieve the NIFTY data from Yahoo finance:
XSHE000002_data = st.get_csv_data('000002.XSHE', 'price')

# Compute the 5-period Rate of Change for NIFTY
n = 5
NIFTY_ROC = ROC(XSHE000002_data, n)
ROC = NIFTY_ROC['Rate of Change']

# Plotting the Price Series chart and the Ease Of Movement below
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(2, 1, 1)
ax.set_xticklabels([])
plt.plot(XSHE000002_data['close'], lw=1)
plt.title('NSE Price Chart')
plt.ylabel('Close Price')
plt.grid(True)
bx = fig.add_subplot(2, 1, 2)
plt.plot(ROC, 'k', lw=0.75, linestyle='-', label='ROC')
plt.legend(loc=2, prop={'size': 9})
plt.ylabel('ROC values')
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()
