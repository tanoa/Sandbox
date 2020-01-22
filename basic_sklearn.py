#基本的な学習とテストの仕方(iris.csv))
#以下からダウンロードする※Rawを選択する
#[httpsgithub.compandas-devpandasblobmasterpandastestsdatairis.csvembedcite]

#ライブラリ読み込み
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# データの読み込み 
iris_data = pd.read_csv(iris.csv, encoding=utf-8)

# データをラベルと入力データに分離
y = iris_data.loc[,Name]
x = iris_data.loc[,[SepalLength,SepalWidth,PetalLength,PetalWidth]]

# 学習用8割とテスト用2割に分離
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, train_size = 0.8, shuffle = True)

# 学習（アルゴリズム指定）
clf = SVC()
clf.fit(x_train, y_train)

# 評価する
y_pred = clf.predict(x_test)
print(正解率 =  , accuracy_score(y_test, y_pred))
