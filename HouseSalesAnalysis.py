# Data Analysis Using Python

# Libraries Used

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import piplite
await piplite.install(['pandas','matplotlib','scikit-learn','seaborn', 'numpy'])
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression

from pyodide.http import pyfetch

# Importing DataSets

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
await download(file_name, "kc_house_data_NaN.csv")
file_name="kc_house_data_NaN.csv"

# Use the Pandas method read_csv() to load the data from the web address.
df = pd.read_csv(file_name)

#To display the first 5 columns of the dataframe.
df.head()

# To obtain a statistical summary of the dataframe.
df.describe()

# Drop the columns "id" and "Unnamed: 0" from axis 1 , then obtain a statistical summary of the data. 
print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())

# Replace the missing values of the column 'bedrooms' and 'bathrooms' with the mean of the column 'bedrooms' and 'bathrooms' respectively
mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)

mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)

print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())

# Count the number of houses with unique floor values,and convert it to a dataframe.
df["floors"].value_counts().to_frame()
df["floors"].head()

### Determine whether houses with a waterfront view or without a waterfront view have more price outliers.
sns.boxplot(x="waterfront",y="price",data=df)

# Determine if the feature sqft_above is negatively or positively correlated with price.
sns.regplot(x="waterfront",y="price",data=df)
plt.ylim(0,)

# Find the feature other than price that is most correlated with price.
df.corr()['price'].sort_values()

# Fit a linear regression model using the longitude feature 'long' and caculate the R^2.
X = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
lm.score(X, Y)

# Fit a linear regression model to predict the 'price' using the feature 'sqft_living' then calculate the R^2. Take a screenshot of your code and the value of the R^2.
S = df[['sqft_living']]
Y = df['price']
lm = LinearRegression()
lm.fit(S,Y)
lm.score(S, Y)
lm.intercept_
lm.coef_
Yhat = lm.predict(S)
print("The value of R^2 : ",lm.score(S, Y), "The Yhat Predict : ", Yhat[0:2])

# Fit a linear regression model to predict the 'price' using the list of features:
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]     
F = df[features]
Y = df['price']
lm.fit(F, Y)
lm.score(F, Y)
Yhat = lm.predict(F)
print("The value of R^2 : ",lm.score(F, Y), "The Yhat Predict : ", Yhat[0:2])

# Create a pipeline object to predict the 'price', fit the object using the features in the list features, and calculate the R^2.
Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]
F = df[features]
F = F.astype(float)
pipe= Pipeline(Input)
pipe.fit(F,Y)
Ypipe = pipe.predict(F)
print("The value of R^2 : ",lm.score(F, Y), "The Ypipe Predict : ", Ypipe[0:2])

# Split the data into training and testing sets
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]    
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)

print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

# Create and fit a Ridge regression object using the training data, set the regularization parameter to 0.1, and calculate the R^2 using the test data.
from sklearn.linear_model import Ridge
RidgeModel = Ridge(alpha= 0.1)
RidgeModel.fit(x_train,y_train)
r_squared = RidgeModel.score(x_test, y_test)
print(r_squared)

# Perform a second order polynomial transform on both the training data and testing data. 
pr_Traindata =pr.fit_transform(x_train)
pr_Testdata =pr.fit_transform(x_test)

RidgeModel = Ridge(alpha= 0.1)
RidgeModel.fit(x_train,y_train)
r_squared = RidgeModel1.score(x_test, y_test)
print(r_squared)








