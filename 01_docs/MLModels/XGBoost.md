# モデルの特徴
[XGBoost](https://xgboost.readthedocs.io/en/latest/index.html)は、Extreme Gradient Boostingの略で、スケーラブルで分散型の勾配ブースト決定木（GBDT）機械学習ライブラリです。並列木ブースティングを提供し、回帰、分類、ランキング問題のための主要な機械学習ライブラリです。

Baseとなっている手法
- Decision Trees
- Enemble Learning
- Gradient Boosting

## 学習のステップ
### STEP1
全ての学習データに対して、等しい重み付けで学習を行い、決定境界を引きます。これを弱学習器による学習と言います。
### STEP2
STEP1で正しく識別されたデータの重みが下げられ、誤って識別されたデータの重みが上げられています。高く重み付けがなされたデータは決定境界で正しく識別されていますが、他のデータは誤って分類されています。
### STEP3
STEP2と同様の傾向があります。このような弱学習器による処理を繰り返すことで識別性能を高めていきます。
### Finally
最終的には最適な決定境界を引くことができるような識別器を求めていきます。

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRT7OVtKPfHy8np0-Y5jMK9uERj6VwqCcu_othIWrR0RAsmf_lb96aDSQOy5bKbedAs4gx3ppgM0ZVa/embed?start=1&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

<!-- # Hyperparamters
## learning_rate
## max_depth
## subsample
## colsample_bytree
## n_estimators
## objective
## gamma
## alpha
## lambda -->

# サンプルコード

```
import xgboost as xgb

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

""" Binary Classification by XGBoost"""
dataset = datasets.load_breast_cancer()
X, y = dataset.data, dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    shuffle=True,
                                                    random_state=42,
                                                    stratify=y)

# scikit-learn API を備えた分類器
clf = xgb.XGBClassifier(objective='binary:logistic',
                        # 'num_boost_round' の代わり
                        # adding 1 estimator per round
                        n_estimators=1000)
# 学習する
evals_result = {}
clf.fit(X_train, y_train,
        # 学習に使う評価指標
        eval_metric='logloss',
        # 学習時に用いる検証用データ
        eval_set=[
            (X_train, y_train),
            (X_test, y_test),
        ],
        early_stopping_rounds=10,
        # 学習過程の記録はコールバック API で登録する
        callbacks=[
            xgb.callback.record_evaluation(evals_result)
        ],
        )

y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print('Accuracy:', acc)

# 学習過程の名前は 'validation_{n}' になる
train_metric = evals_result['validation_0']['logloss']
plt.plot(train_metric, label='train logloss')
eval_metric = evals_result['validation_1']['logloss']
plt.plot(eval_metric, label='eval logloss')
plt.grid()
plt.legend()
plt.xlabel('rounds')
plt.ylabel('logloss')
plt.show()

```

# References
- [Using XGBoost in Python Tutorial](https://www.datacamp.com/community/tutorials/xgboost-in-python)
- [XGBoost論文を丁寧に解説する(1)](https://qiita.com/triwave33/items/aad60f25485a4595b5c8#gradient-tree-boosting)
