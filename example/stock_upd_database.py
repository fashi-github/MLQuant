import datetime

import pandas as pd

import data.stock as st

code = '000002.XSHG'

# data = st.get_single_price(code=code,
#                            time_freq='daily',
#                            start_date='2021-01-01',
#                            end_date='2021-02-01')
# st.export_data(data=data, filename=code, type='price')
#
# data = st.get_csv_data(code=code, type='price')
# print(data)
# st.init_db()

stocks = st.get_stock_list()
for code in stocks:
    st.update_daily_price(code, 'price')
# df = st.get_single_price('000024.XSHE', 'daily', '2018-12-26', datetime.datetime.today())
# print(df)
# print('\n\n\n')
# print(df.dropna())

# 1 获取所有股票代码

# 2 存储到CSV文件中

# 3 每日更新数据：
# 3.1 获取增量数据
# 3.2 追加到已有文件中

