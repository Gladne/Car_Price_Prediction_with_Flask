import pandas as pd
df = pd.read_csv('/home/bellona/Documents/Web Development/Flask/Flask _Car_project/cleaned_car_data.csv')

X=df[['Present_Price', 'Kms_Driven',
       'Car_Age', 'Fuel_Type_CNG', 
       'Fuel_Type_Diesel', 'Fuel_Type_Petrol', 
       'Transmission_Automatic', 'Transmission_Manual'
]]

y = df['Selling_Price']

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)

import pickle
with open('lr_model.pkl', 'wb') as model_file: # wb - write binary
    pickle.dump(model, model_file)