from data.stock import get_csv_data


def get_real_result(stock_code):
    stock_data = get_csv_data(stock_code, 'price')
    close_price = stock_data['close']
    print(close_price.head(10))
    print(close_price.tail(10))
    real_result = close_price.shift(-1)
    print(real_result.head(10))
    print(real_result.tail(10))
    real_result = real_result.dropna()
    print(real_result.tail(10))
    return real_result

stock_code = '000002.XSHE'
get_real_result(stock_code)
