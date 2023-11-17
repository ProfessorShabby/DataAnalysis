# Import the required libraries
import pandas as pd
dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"

# Load the data available at dataset_url into a dataframe.

csv = pd.read_csv(dataset_url)
Data = pd.DataFrame(csv)

# Display the top 5 rows and columns from your dataset.
Data.head()

# Print the number of rows in the dataset.
rows = len(Data.axes[0])
print("Rows:" + str(rows))

# Print the number of columns in the dataset.
cols = len(Data.axes[1])
print("Columns:" + str(cols))

# Print the datatype of all columns.
print(Data.dtypes)

# Print the mean age of the survey participants.
print(Data['Age'].mean())

# Print how many unique countries are there in the Country column.
print(Data['Country'].unique())
