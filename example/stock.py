import data.stock as st

data = st.get_single_price('000001.XSHE',
                           'daily',
                           '2020-01-01',
                           '2020-02-01')
# print(data)

data = st.calculate_change_pct(data)
# print(data)
 
# 获取周K
data = st.transfer_price_freq(data, 'w')
print(data)

data = st.calculate_change_pct(data)
print(data)

