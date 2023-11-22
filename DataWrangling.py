# Import pandas module.
import pandas as pd

# Load the dataset into a dataframe.
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")
df.head(10)

# Finding duplicates
# Find how many duplicate rows exist in the dataframe.
len(df[df.duplicated()])

# Removing duplicates
# Remove the duplicate rows from the dataframe.
df.drop_duplicates()

# Verify if duplicates were actually dropped.
df.duplicated(subset=None, keep='first').sum()

# Finding Missing values
# Find the missing values for all columns.
df.isnull()

# Find out how many rows are missing in the column 'WorkLoc'
df['WorkLoc'].isnull().sum()

# Find the value counts for the column WorkLoc.
df['WorkLoc'].value_counts()

# Identify the value that is most frequent (majority) in the WorkLoc column.
Majority = df['WorkLoc'].value_counts().idxmax()
print(Majority)

# Impute (replace) all the empty rows in the column WorkLoc with the value that you have identified as the majority.
df['WorkLoc'].dropna(inplace=True)
df['WorkLoc'].replace('',"Office", inplace=True)

# Normalizing data
# There are two columns in the dataset that talk about compensation. One is "CompFreq". This column shows how often a developer is paid (Yearly, Monthly,Weekly).
# The other is "CompTotal". This column talks about how much the developer is paid per Year, Month, or Week depending upon his/her "CompFreq".
# This makes it difficult to compare the total compensation of the developers.

# List out the various categories in the column 'CompFreq'
list(df['CompFreq'].value_counts().index)
df['CompFreq'].value_counts()

# Create a new column named 'NormalizedAnnualCompensation'. Use the hint given below if needed.
List = []
#new_df[column] = 'NormalizedAnnualCompensation'
for cell1, cell2 in zip(new_df['CompFreq'],new_df['CompTotal']):
  if cell1 == "Yearly":
    List.append(cell2)
  elif cell1 == "Monthly":
    List.append(12*cell2)
  elif cell1 == "Weekly":
    List.append(52*cell2)
new_df['NormalizedAnnualCompensation'] = List
new_df['NormalizedAnnualCompensation']
new_df['NormalizedAnnualCompensation'].median()









