# Collect the number of job postings for the following languages using the API:

# C
# C#
# C++
# Java
# JavaScript
# Python
# Scala
# Oracle
# SQL Server
# MySQL Server
# PostgreSQL
# MongoDB

# Import required libraries
import requests
baseurl = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/datasets/githubposting.json"

resp = requests.get(baseurl)

if resp.ok:
    data=resp.json()

# Write a function to get the number of jobs for the given technology.

def get_number_of_jobs(technology):
    number_of_jobs = 0
    for tech in technology:
        number_of_jobs = number_of_jobs + 1
    return technology,number_of_jobs
  
# Call the function for Python and check if it is working.

print(get_number_of_jobs('python'))

# Create a python list of all technologies for which you need to find the number of jobs postings.
Jobs = ['C','C#','C++','Java','JavaScript','Python','Scala','Oracle','SQL Server','MySQL Server','PostgreSQL','MongoDB']

# Import libraries required to create excel spreadsheet
!pip install openpyxl
from openpyxl import Workbook

# Create a workbook and select the active worksheet
wb=Workbook()                        
ws=wb.active

# Find the number of jobs postings for each of the technology in the above list. Write the technology name and the number of jobs postings into the excel spreadsheet.
for job in Jobs:
    print(get_number_of_jobs(job))
    ws.append(get_number_of_jobs(job))

# Save into an excel spreadsheet named 'github-job-postings.xlsx'.
wb.save('github-job-posting.xlsx'



