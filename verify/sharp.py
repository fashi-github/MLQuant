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
big_increase_pct = pd.DataFrame()
# profit_pct = pd.DataFrame({'percent': 0}, index=[1000])
percent_index = 0
percent_array = list()
big_increase_array = list()
pred_cnt = 0
big_increase_cnt = 0
pred_big_increase_cnt = 0
real_big_increase_cnt = 0
for i, close in test_y.items():
    if pred_index >= pred_y.size:
        break
    # print('pred_y', pred_y[pred_index])
    # print('pred_y size: ', pred_y.size)
    # print('test_y size: ', test_y.size)
    if pred_y[pred_index] >= close * 1.05:
        pred_big_increase_cnt = pred_big_increase_cnt + 1
        # print('index: ', i, 'value: ', close, 'prev value:', test_y[i])
        if i >= 4024:
            break
        # test_y[i + 1]就是close的下一天的收盘价格
        percent = (test_y[i + 1] - close) / close
        if percent >= 0.05:
            big_increase_array.append(percent)
            real_big_increase_cnt = real_big_increase_cnt + 1
        pred_cnt = pred_cnt + 1
        # print("predict right !!", percent)
        # if percent > 0:
        percent_array.append(percent)
        # percent_index = percent_index + 1
    pred_index = pred_index + 1

profit_pct['percent'] = percent_array
print('predict correctly percent: ', float(pred_cnt / pred_index))
print('profit mean: ', profit_pct.mean())
big_increase_pct['percent'] = big_increase_array
print('big increase profit mean: ', big_increase_pct.mean())

avg_return = profit_pct.mean()
sd_reutrn = profit_pct.std()
# 计算夏普：每日收益率 * 252 = 每年收益率
sharpe = avg_return / sd_reutrn
print('Sharp: ', sharpe)

avg_big_return = big_increase_pct.mean()
std_big_return = big_increase_pct.std()
print('Big Sharp: ', avg_big_return / std_big_return)
print('big increase percent:\n', big_increase_pct)
print('big increase correct percent:\n', real_big_increase_cnt / pred_big_increase_cnt)
# for index, row in test_y.iterrows():
#     print(index, row[''])


# for i in pred_y:
#     if(i )
