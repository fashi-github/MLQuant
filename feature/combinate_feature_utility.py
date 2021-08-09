import pandas as pd

from feature.CCI import get_cci
from feature.evm import get_evm
from feature.BB import get_lower_bb, get_upper_bb
from feature.FI import get_force_index
from feature.MA import get_sma, get_ewma
from feature.ROC import get_roc

stock_code = '000002.XSHE'


def get_total_x():
    mix = get_cci(stock_code, 20)
    # evm间隔性为空，14个为空接着若干个有数值。
    evm = get_evm(stock_code, 14)
    mix['evm'] = evm
    mix['FI'] = get_force_index(stock_code, 1)
    mix['ROC'] = get_roc(stock_code, 5)
    mix['SMA'] = get_sma(stock_code, 50)
    # mix['EWMA'] = get_ewma(stock_code, 200)
    mix['Lower BollingerBand'] = get_lower_bb(stock_code, 50)
    mix['Upper BollingerBand'] = get_upper_bb(stock_code, 50)
    mix = mix.fillna(method='bfill')
    # 此处做去除最后一行的操作，是为了和预测值对齐？？？？
    # mix = mix[:-1]
    total = mix.drop(columns=['date'])
    print('total: ', total.shape)
    return total
    # mix = (pd.Series(cci, name='CCI')).join(pd.Series(evm, name='evm'))
    # print(mix)

# get_total_x()
# evm = get_evm(stock_code, 14)
# print(evm.head(50))
