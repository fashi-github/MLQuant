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
# 因为在模型里面已经做了对齐，所以预测的索引就从零开始
pred_index = 0
profit_pct = pd.DataFrame()
# profit_pct = pd.DataFrame({'percent': 0}, index=[1000])
percent_index = 0
percent_array = list()
for i, close in test_y.items():
    if pred_index >= pred_y.size:
        break
    # print('pred_y', pred_y[pred_index])
    # print('pred_y size: ', pred_y.size)
    # print('test_y size: ', test_y.size)
    if pred_y[pred_index] > close:
        # print('index: ', i, 'value: ', close, 'prev value:', test_y[i])
        if i >= 4024:
            break
        # test_y[i + 1]就是close的下一天的收盘价格
        percent = (test_y[i + 1] - close) / close
        # print("predict right !!", percent)
        # print("predict df !!", pd.DataFrame(
        #     {'percent': percent},
        #     index=[percent_index]))
        # profit_pct.append(pd.DataFrame(
        #     {'percent': percent},
        #     index=[percent_index]))
        # if percent > 0:
        percent_array.append(percent)
        # percent_index = percent_index + 1
    pred_index = pred_index + 1

profit_pct['percent'] = percent_array
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
