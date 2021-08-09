import datetime

import pandas as pd
from jqdatasdk import *
import os

auth('13520837980', 'Guo1220!')
pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_columns', 1000)
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))#获取项目根目录
data_root = os.path.join(PROJECT_ROOT, "") #文件路径
# data_root = '/Users/wizard/Documents/BigData/PythonProject/WizardQuantGithub/data/'


def init_db():
    stocks = get_stock_list()
    for code in stocks:
        df = get_single_price(code, 'daily')
        export_data(df, code, 'price')
        print(code)
        print(df.head())

def get_stock_list():
    stocks_list = list(get_all_securities('stock').index)
    print(stocks_list)
    return stocks_list


def get_single_price(code, time_freq, start_date=None, end_date=None):
    # 如果start_date为空，默认为从上市日期开始
    if start_date is None:
        start_date = get_security_info(code).start_date
    if end_date is None:
        end_date = datetime.datetime.today()
    data = get_price(code,
                     start_date=start_date,
                     end_date=end_date,
                     frequency=time_freq,
                     panel=False)
    return data


# mode: 用a代码追加，none代表全量写入
def export_data(data, filename, type, mode=None):
    file_root = data_root + type + '/' + filename + '.csv'
    data.index.names = ['date']
    if mode == 'a':
        data.to_csv(file_root, mode=mode, header=False)
        data = pd.read_csv(file_root)
        data = data.drop_duplicates(subset=['date'])
        data.to_csv(file_root)
        print('成功更新存储至：', file_root)
    else:
        data.to_csv(file_root)
        print('成功生成存储至：', file_root)


def get_csv_data(code, type):
    file_root = data_root + type + '/' + code + ".csv"
    if os.path.exists(file_root):
        total = pd.read_csv(file_root)
        # 因为2017年之前的数据，存在成交量为零的情况，
        # 所以为了数据的高质量，从2017年开始获取数据。
        quality_data = total[total['date'].str.startswith('2017') |
                             total['date'].str.startswith('2018') |
                             total['date'].str.startswith('2019') |
                             total['date'].str.startswith('202')]
        print(quality_data.head(10))
        print(quality_data.tail(10))
        print(quality_data.shape)
        return quality_data
    else:
        print('NOT find ' + file_root)
        return None


def transfer_price_freq(data, time_freq):
    """
    将数据转换为制定周期：开盘价（周期第1天）、收盘价（周期最后1天）、最高价（周期内）、最低价（周期内）
    :param data:
    :param time_freq:
    :return:
    """
    df_trans = pd.DataFrame()
    df_trans['open'] = data['open'].resample(time_freq).first()
    df_trans['close'] = data['close'].resample(time_freq).last()
    df_trans['high'] = data['high'].resample(time_freq).max()
    df_trans['low'] = data['low'].resample(time_freq).min()

    return df_trans


def get_single_finance(code, date, statDate):
    data = get_fundamentals(query(indicator).filter(indicator.code == code),
                            date=date,
                            statDate=statDate)
    return data


def get_single_valuation(code, date, statDate):
    data = get_fundamentals(query(valuation).filter(valuation.code == code),
                            date=date,
                            statDate=statDate)
    return data


def calculate_change_pct(data):
    data['close_pct'] = (data['close'] - data['close'].shift(1)) / data['close'].shift(1)
    return data


def update_daily_price(stock_code, type):
    file_root = data_root + type + '/' + stock_code + '.csv'
    if os.path.exists(file_root):
        # 获取增量数据
        startdate = pd.read_csv(file_root, usecols=['date'])['date'].iloc[-1]
        # df = get_single_price(stock_code, 'daily', startdate, datetime.datetime.today())
        print('NOT update for ' + stock_code)
        # export_data(df, stock_code, 'price', 'a')
        # df.index.names = ['date']
        # df = df.drop_dulicates(subset=['date'], keep='last')
        # df.to_csv(file_root, mode='a', header=False)
    else:
        # 重新获取全量
        df = get_single_price(stock_code, 'daily')
        export_data(df, stock_code, 'price', 'none')

# stocks = list(get_all_securities('stock').index)
# print(stocks)

df = get_price('000001.XSHG',
               end_date='2021-02-22',
               count=20,
               frequency='daily',
               fields=['open', 'close', 'high', 'low', 'volume', 'money'],
               panel=False)
# df['weekday'] = df.index.weekday
# print(df)

# 获取周K
# df_week = pd.DataFrame()
# df_week['open'] = df['open'].resample('W').first()
# print(df_week)

# 汇总统计
# df_week['volume(sum)'] = df['volume'].resample('W').sum()
# df_week['volume(sum)'] = df['money'].resample('W').sum()
# print(df_week)

# 获取股票财务指标
# df = get_fundamentals(query(indicator),
#                       statDate='2020')
# print(df)
# df.to_csv("C:/Users/wangh/PycharmProjects/WizardQuant/data/finance/finance2020.csv")

# df_valuation = get_fundamentals(query(valuation), statDate=datetime.datetime.today())
# df_valuation.index = df_valuation['code']
# print(df_valuation.head())
# df['pe_ratio'] = df_valuation['pe_ratio']
# print(df.head())
