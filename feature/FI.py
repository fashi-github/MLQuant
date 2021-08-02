################# Force Index ########################################################

# Load the necessary packages and modules
import pandas as pd
import data.stock as st


# Force Index
def ForceIndex(data, ndays):
    FI = pd.Series(data['close'].diff(ndays) * data['volume'], name='ForceIndex')
    data = data.join(FI)
    return data


def get_force_index(stock_code, ndays):
    stock_data = st.get_csv_data(stock_code, 'price')
    merged_data = ForceIndex(stock_data, ndays)
    return merged_data['ForceIndex']


XSHE000002_data = st.get_csv_data('000002.XSHE', 'price')


# Compute the Force Index for Apple 
n = 1
AAPL_ForceIndex = ForceIndex(XSHE000002_data, n)
print(AAPL_ForceIndex['ForceIndex'])
