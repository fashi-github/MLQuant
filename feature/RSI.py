import numpy as np
import pandas as pd
import data.stock as st


def rsi(price, period=6):
    clprcChange = price - price.shift(1)
    clprcChange = clprcChange.dropna()
    indexprc = clprcChange.index
    upPrc = pd.Series(0, index=indexprc)
    upPrc[clprcChange > 0] = clprcChange[clprcChange > 0]
    downPrc = pd.Series(0, index=indexprc)
    downPrc[clprcChange < 0] = -clprcChange[clprcChange < 0]
    rsidata = pd.concat([price,
                         clprcChange,
                         upPrc,
                         downPrc],
                        axis=1)
    rsidata.columns = ['price', 'PrcChange', 'upPrc', 'downPrc']
    rsidata = rsidata.dropna();
    SMUP = []
    SMDOWN = []
    for i in range(period, len(upPrc) + 1):
        SMUP.append(np.mean(upPrc.values[(i - period):i],
                            dtype=np.float32))
        SMDOWN.append(np.mean(downPrc.values[(i - period):i],
                              dtype=np.float32))
        rsi = [100 * SMUP[i] / (SMUP[i] + SMDOWN[i])
               for i in range(0, len(SMUP))]
    indexRsi = indexprc[(period - 1):]
    rsi = pd.Series(rsi, index=indexRsi)
    return rsi


def get_rsi(stock_code):
    stock_data = st.get_csv_data(stock_code, 'price')
    BOCMclp = stock_data['close']
    Rsi12 = rsi(BOCMclp, 12)
    return Rsi12


# Rsi12 = get_rsi('000002.XSHE')
# print(Rsi12.tail())
