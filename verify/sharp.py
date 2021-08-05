import pandas as pd

import global_value
import global_value as glob
from model import grid_search
import numpy as np

grid_search.perform()
test_y = glob.get_value(glob.TEST_Y)
print(test_y.tail(10))
# pred_y is array
pred_y = glob.get_value(glob.PRED_Y)
j = 1
profit_pct = pd.DataFrame()
# profit_pct = pd.DataFrame({'percent': 0}, index=[1000])
percent_index = 0
percent_array = list()
for i, close in test_y.items():
    print('pred_y', pred_y[j])
    print('pred_y size: ', pred_y.size)
    print('test_y size: ', test_y.size)
    if j >= pred_y.size:
        break
    if pred_y[j] > close:
        print('index: ', i, 'value: ', close, 'prev value:', test_y[i ])
        if i >= 4023:
            break
        percent = (test_y[i + 1] - close) / close
        print("predict right !!", percent)
        # print("predict df !!", pd.DataFrame(
        #     {'percent': percent},
        #     index=[percent_index]))
        # profit_pct.append(pd.DataFrame(
        #     {'percent': percent},
        #     index=[percent_index]))
        percent_array.append(percent)
        # percent_index = percent_index + 1
    j = j + 1

print('percent list:', percent_array)
profit_pct['percent'] = percent_array
print(profit_pct)
print('profit mean: ', profit_pct.mean())

avg_return = profit_pct.mean()
sd_reutrn = profit_pct.std()
# 计算夏普：每日收益率 * 252 = 每年收益率
sharpe = avg_return / sd_reutrn
print('Sharp: ', sharpe)
# for index, row in test_y.iterrows():
#     print(index, row[''])


# for i in pred_y:
#     if(i )
