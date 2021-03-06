import pandas as pd

from CCI import get_cci
from evm import get_evm
from feature.BB import get_lower_bb, get_upper_bb
from feature.FI import get_force_index
from feature.MA import get_sma
from feature.ROC import get_roc

stock_code = '000002.XSHE'
mix = get_cci(stock_code, 20)
# print(cci.head(20))

evm = get_evm(stock_code, 14)
# print(evm.head(20))
mix['evm'] = evm
mix['FI'] = get_force_index(stock_code, 1)
mix['ROC'] = get_roc(stock_code, 5)
mix['SMA'] = get_sma(stock_code, 50)
mix['Lower BollingerBand'] = get_lower_bb(stock_code, 50)
mix['Upper BollingerBand'] = get_upper_bb(stock_code, 50)
print(mix.head(70))
# mix = (pd.Series(cci, name='CCI')).join(pd.Series(evm, name='evm'))
# print(mix)
