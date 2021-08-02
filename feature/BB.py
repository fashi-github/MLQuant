################ Bollinger Bands #############################

# Load the necessary packages and modules
import pandas as pd
import data.stock as st


# Compute the Bollinger Bands 
def BBANDS(data, ndays):
    MA = pd.Series(data['close'].rolling(ndays).mean())
    # MA = pd.Series(pd.rolling_mean(data['Close'], ndays))
    # SD = pd.Series(pd.rolling_std(data['Close'], ndays))
    SD = pd.Series(data['close'].rolling(ndays).std())

    b1 = MA + (2 * SD)
    B1 = pd.Series(b1, name='Upper BollingerBand')
    data = data.join(B1)

    b2 = MA - (2 * SD)
    B2 = pd.Series(b2, name='Lower BollingerBand')
    data = data.join(B2)

    return data


def get_lower_bb(stock_code, ndays):
    stock_data = st.get_csv_data(stock_code, 'price')
    bb = BBANDS(stock_data, ndays)
    return bb['Lower BollingerBand']


def get_upper_bb(stock_code, ndays):
    stock_data = st.get_csv_data(stock_code, 'price')
    bb = BBANDS(stock_data, ndays)
    return bb['Upper BollingerBand']

# # Retrieve the Nifty data from Yahoo finance:
# XSHE000002_data = st.get_csv_data('000002.XSHE', 'price')
#
# # Compute the Bollinger Bands for NIFTY using the 50-day Moving average
# n = 50
# NIFTY_BBANDS = BBANDS(XSHE000002_data, n)
# print(NIFTY_BBANDS)
