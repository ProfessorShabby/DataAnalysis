# Data Analysis Using Python

### Libraries Used

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

### Importing DataSets

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
await download(file_name, "kc_house_data_NaN.csv")
file_name="kc_house_data_NaN.csv"

### Use the Pandas method read_csv() to load the data from the web address.
df = pd.read_csv(file_name)

###To display the first 5 columns of the dataframe.
df.head()

### To obtain a statistical summary of the dataframe.
df.describe()

### Drop the columns "id" and "Unnamed: 0" from axis 1 , then obtain a statistical summary of the data. 
print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())

### Replace the missing values of the column 'bedrooms' and 'bathrooms' with the mean of the column 'bedrooms' and 'bathrooms' respectively
mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)

mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)

print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())





