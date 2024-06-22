import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Load the dataset
data = pd.read_csv('day5\Housing.csv')
data.replace({'yes': 1, 'no': 0, 'furnished':1, 'semi-furnished':2, 'unfurnished':0 },inplace=True)

print(data.head())


x=data[['area','bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']]
y=data['price']
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2,random_state=10)
model = LinearRegression()
model.fit(X_train,Y_train)
res = model.score(X_test,Y_test)
print(res)

area = int(input("Enter area size : "))
bedrooms = int(input("Number of bedrooms : "))
bathrooms = int(input("Number of bathrooms : "))
stories = int(input("Number of Stories : "))
mainroad = int(input("Infront of main road (yes:1 or No:0) : "))
guestroom = int(input("Want guestroom (yes:1 or No:0) : "))
basement = int(input("Want Basement (yes:1 or No:0) : "))
hotwaterheating = int(input("Need water heater (yes:1 or No:0) : "))
airconditioning = int(input("Need airconditioning (yes:1 or No:0) : "))
parking = int(input("Need parking (yes:1 or No:0) : "))
prefarea = int(input("Near urban  (yes:1 or No:0) : "))
furnishingstatus = int(input("Furnishing status (furnished:1, unfurnished:0, semi-furnished:2)) : "))

predicted_price =  model.predict([[area  ,bedrooms  ,bathrooms  ,stories  ,mainroad  ,guestroom  ,basement  ,hotwaterheating  ,airconditioning  ,parking  ,prefarea  ,furnishingstatus]])

print(f"""
      -------------------------------
      -------------------------------
      Predicted Price : 

      ₹ { str(int(predicted_price))}
      
      -------------------------------
      -------------------------------
      """)

print(f"predection accuracy : {(model.score(X_test, Y_test))*100}%")

