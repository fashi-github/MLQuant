from typing import Any, Union

import pandas as pd
from pandas import Series, DataFrame
from pandas.core.arrays import ExtensionArray
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

from feature import combinate_feature_utility
from train import resultY
from sklearn import preprocessing
from sklearn.metrics import r2_score
import global_value as glob


def perform():
    tuned_parameters = [
        {'alpha': [1, 0.5, 0.1, 0.01, 0.001]}
    ]
    model = GridSearchCV(Ridge(), tuned_parameters, cv=10)
    total_x = combinate_feature_utility.get_total_x()
    total_y = resultY.get_real_result('000002.XSHE')
    train_x = total_x[0:3000]
    train_y = total_y[0:3000]
    print(total_x.shape)
    print(total_y.shape)
    print(train_x.shape)
    print(train_y.shape)
    # scaler = preprocessing.StandardScaler().fit(train_x)
    # X = scaler.transform(train_x)
    # X[:10,:]

    model.fit(train_x, train_y)

    print("Optimised parameters found on training set:")
    print(model.best_estimator_, "\n")

    print("Grid scores calculated on training set:")
    print(model.best_estimator_)
    print(model.best_score_)
    # for params, mean_score, scores in model.cv_results_:
    #     print("%0.3f for %r" % (mean_score, params))

    test_x = total_x[3001:4025]
    test_y = total_y[3001:4025]
    glob._init()
    glob.set_value(glob.TEST_Y, test_y)
    pred_y = model.predict(test_x)
    print('pred_y', pred_y)
    glob.set_value(glob.PRED_Y, pred_y)
    print('R2 Score:', r2_score(test_y, pred_y))
    df_result = pd.DataFrame(index=test_y.index)
    df_result['True Value'] = test_y
    df_result['Pred Value'] = pred_y
    df_result.plot(figsize=(16, 9))
