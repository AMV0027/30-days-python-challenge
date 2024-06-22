import pandas as pd
import numpy as np
import pyfiglet 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

font = pyfiglet.figlet_format("Tesla Stock Analysis")
print(font)

data = pd.read_csv('day7/tesla.csv')
data['Date'] = pd.to_datetime(data['Date'])

data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

x = data[['High', 'Low', 'Year', 'Month', 'Day']]
y = data['Close']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)


model = LinearRegression()
model.fit(X_train, y_train)


res = model.score(X_test, y_test)
print("Model Accuracy:", int(float(res)*100), "%")

date = input("\nEnter date to predict Tesla price\nEg. (2005-01-27) : ")

future_date = pd.to_datetime(date)
future_features = np.array([[100, 90, future_date.year, future_date.month, future_date.day]])  # Use arbitrary values for High and Low
predicted_price = model.predict(future_features)
print("\n\n")
price  = pyfiglet.figlet_format("$ "+str(round(predicted_price[0],2)), font = "digital")
print(price)
print("-----\nPredicted Price for {}: ${:.2f}".format(future_date.date(), predicted_price[0] ,"\n-----"))
