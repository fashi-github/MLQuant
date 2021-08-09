from data.stock import get_csv_data


def get_real_result(stock_code):
    stock_data = get_csv_data(stock_code, 'price')
    # print('stock data tail\n', stock_data)
    # close_price = stock_data['close']
    # print('close price head\n', close_price.head(10))
    # print('close price tail\n', close_price.tail(10))
    # real_result = close_price.shift(-1)
    # print('close price head shift -1\n', real_result.head(10))
    # print('close price tail shift -1\n', real_result.tail(10))
    # real_result = real_result.dropna()
    # print('result data tail\n', real_result.tail(10))
    return stock_data['close']

stock_code = '000002.XSHE'
get_real_result(stock_code)
