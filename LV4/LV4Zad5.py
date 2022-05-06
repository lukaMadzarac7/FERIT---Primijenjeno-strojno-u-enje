from random import random
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
import sklearn.linear_model as lm

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, max_error
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LinearRegression

#ucitavanje
df = pd.read_csv('cars_processed.csv')
print(df.info())
#brisanje nepotrebnih stupaca
df = df.drop(['name', 'mileage'], axis=1)
#odabir ulaza/izlaza
x = df[['km_driven', 'year', 'engine', 'max_power']]
y = df['selling_price']
#podjela train/test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)
print(x_train.shape)
#skaliranje
Scaler = MinMaxScaler()
x_train_s = Scaler.fit_transform(x_train)
x_test_s = Scaler.transform(x_test)
#izrada modela
linear_model = LinearRegression
linear_model.fit(x_train_s, y_train)
#evaluacija modela
y_pred_train = linear_model.predict(x_train_s)
y_pred_test = linear_model.predict(x_test_s)

print("R2 test", r2_score(y_pred_test, y_test))
print("RMSE test:", np.sqrt(mean_squared_error(y_pred_test, y_test)))
print("Max error test:", max_error(y_pred_test, y_test))
print("MAE test:", mean_absolute_error(y_pred_test, y_test))

