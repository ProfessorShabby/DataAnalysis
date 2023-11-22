# Import the pandas module.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the dataset into a dataframe.

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")
df.head()

# Distribution
# Determine how the data is distributed. The column ConvertedComp contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.
# This assumes 12 working months and 50 working weeks.

# Plot the distribution curve for the column ConvertedComp.
sns.displot(data = df['ConvertedComp'], kind = "kde", color = 'green')

# Plot the histogram for the column ConvertedComp.
sns.histplot(data = df['ConvertedComp'], bins = 50)

# What is the median of the column ConvertedComp?
df['ConvertedComp'].median()

# How many responders identified themselves only as a Man?
df['Gender'].value_counts()

# Find out the median ConvertedComp of responders identified themselves only as a Woman?
df_Gen_W = df[df['Gender']== 'Woman']
df_Gen_W['ConvertedComp'].median()

# Give the five number summary for the column Age?
df['Age'].describe()

# Plot a histogram of the column Age.
sns.histplot(data = df['Age'])

# Find out if outliers exist in the column ConvertedComp using a box plot?
df['Age'].plot(kind='box', color='red', vert=True)

# Find out the Inter Quartile Range for the column ConvertedComp.
quartiles = df['ConvertedComp'].quantile([0.25, 0.75])
iqr = quartiles[0.75] - quartiles[0.25]
print(iqr)

# Find out the upper and lower bounds.
upper = quartiles[0.75]
lower = quartiles[0.25]
​
upperbound = upper +1.5 * iqr
lowerbound = lower - 1.5 * iqr
​
print(upperbound, lowerbound)

# Identify how many outliers are there in the ConvertedComp column.
i = 0
count = 0
for i in df['ConvertedComp']:
    if i > upperbound or i < lowerbound:
        count = count +1
print(count)

# Create a new dataframe by removing the outliers from the ConvertedComp column.
list = []
i = 0
count = 0
for i in df['ConvertedComp']:
    if i < upperbound and i > lowerbound:
        list.append(i)
df1 = pd.DataFrame(list)
df1.columns = ['NewConvertedComp']
df1

# Find the correlation between Age and all other numerical columns.
df.corr()['Age']






