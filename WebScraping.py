# Extract information from the given web site
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

# Import the required libraries
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

# Download the webpage at the url
data  = requests.get(url).text 

# Create a soup object

soup = BeautifulSoup(data,"html.parser") 

# Scrape the Language name and annual average salary.
table = soup.find('table') # in html table is represented by the tag <table>
List = []
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[1].getText() # store the value in column 3 as color_name
    color_code = cols[3].getText() # store the value in column 4 as color_code
    #Result_csv = "{}--->{}".format(color_name,color_code))
    List.append(color_name+", "+color_code)
print(List)


# Save the scrapped data into a file named popular-languages.csv

df = pd.DataFrame(List)
df.to_csv('popular-languages.csv', index=False)
​
    
