import statsmodels.tsa.stattools as stattools
import data.stock as st
import pandas as pd

stock_data = st.get_csv_data('000002.XSHE', 'price')

test_result = stattools.adfuller(stock_data['close'], 1)
print('ADF Result max lag = 1: ', test_result)
test_result = stattools.adfuller(stock_data['close'], autolag='AIC')
print('ADF Result autolag = AIC: ', test_result)
adf = test_result[0]
cv5 = test_result[4]['5%']
print('ADF:', adf, 'CV_%5:', cv5)

stocks = st.get_stock_list()
for code in stocks:
    stock_data = st.get_csv_data(code, 'price')
    if stock_data is not None:
        valid_stock_data = stock_data.dropna()
    if valid_stock_data['close'] is not None:
        print(code)
        adf_result = stattools.adfuller(valid_stock_data['close'], 1)
        adf = adf_result[0]
        cv5 = adf_result[4]['5%']
        if adf < cv5:
            print('时间序列平稳 ' + '\n')
            dfoutput = pd.Series(adf_result[0:4],
                                 index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
            # print(dfoutput)
            for key, value in adf_result[4].items():
                dfoutput['Critical Value (%s)' % key] = value
                print(dfoutput)

stock_data = st.get_csv_data('003000.XSHE', 'price')
if stock_data is None:
    print('003000.XSHE NOT found')
