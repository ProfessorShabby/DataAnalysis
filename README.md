# Detecting Credit Card Fraud

## Scenario
Companies today are employing analytical techniques for the early detection of credit card frauds, a key factor in mitigating fraud damage. The most common type of credit card fraud does not involve the physical stealing of the card, but that of credit card credentials, which are then used for online purchases.

Imagine that you have been hired as a Data Analyst to work in the Credit Card Division of a bank. And your first assignment is to join your team in using data analysis for the early detection and mitigation of credit card fraud.  

In order to prescribe a way forward, that is, suggest what should be done in order for fraud to get detected early on, you need to understand what a fraudulent transaction looks like. And for that you need to start by looking at historical data. 

Here is a sample data set that captures the credit card transaction details for a few users.

![RT7W3bteTX2-1t27Xr19Tw_27ccfcd2e65b4752920e81fda1ae8c5d_DA_1-Image_DataSet_Reading](https://github.com/ProfessorShabby/DataAnalysis/assets/106133748/88265a19-d406-484e-b181-400aeff0e5f4)

Here is a sample visualization that you would use to capture a trend hidden in the sample data set shared.

![kumNKCbZSdqpjSgm2Ynaxw_0326b11a493e49e1b10bc7b2a1f5d7e2_DA_1-Q9-Chart](https://github.com/ProfessorShabby/DataAnalysis/assets/106133748/0cd463ae-df47-4e83-bea0-fcf1591b2853)


# Cleaning and Preparing Data

## Scenario
A recently hired Junior Data Analyst in a local government office has been tasked with importing some data from another department which relates to inventory information about their fleet of vehicles. The data is in comma-separated value (CSV) format and the data also needs cleaning up before you can start to run any kind of analysis on it.

The dataset used in this lab comes from the following source: https://data.montgomerycountymd.gov/Government/Fleet-Equipment-Inventory/93vc-wpdr under a Public Domain license.

### Tasks to perform:

**Save** the CSV file as an XLSX file: Change the ‘Viewing’ in the ToolTip to ‘Editing’inorder to save the file as an XLSX file. The file is converted when you click ‘Convert’ in the prompt.

**Column widths:** Sort out the widths of all columns so that the data is clearly visible in all cells. 

**Empty rows:** Use the Filter feature to look for blanks and remove all empty rows from the data.

**Duplicate records:** Use either the Conditional Formatting or Remove Duplicates feature to look for and remove any duplicated records from the data.

**Spelling:** The original source file data has not been checked for errors in the spelling. Check for spelling mistakes in the data and fix them. 

**Whitespace:** Use the Find and Replace feature to remove all double-spaces from the data.

**Department names:** When the data was converted from its data source, the department names (see correct list below) didn’t import correctly and they are now split over two columns in the data. Use Flash Fill to reduce the department names to just one column, and then remove any unnecessary columns.


    | **Department** | **Department** |
    | ------ | ------ |
    | Board of Elections | Economic Development |
    | Circuit Court | Environmental Protection |
    | Community Engagement Cluster | Finance |
    | Community Use of Public Facilities | Fire and Rescue |
    | Consumer Protection | General Services |
    | Correction and Rehabilitation | Health and Human Services |
    | County Executives Office |  |       



The xlsx files are at https://github.com/ProfessorShabby/DataAnalysis/blob/main/Cleaning%20and%20Preparing%20Data_1.XLSX.xlsx and 
https://github.com/ProfessorShabby/DataAnalysis/blob/main/Cleaning%20and%20Preparing%20Data_2.xlsx.xlsx


# Data Analysis Using SQL

## Data Sets
    
**1. Socioeconomic Indicators in Chicago** : https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2
This dataset contains a selection of six socioeconomic indicators of public health significance and a “hardship index,” for each Chicago community area, for the years 2008 – 2012.

**2. Chicago Public Schools** : https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t
This dataset shows all school level performance data used to create CPS School Report Cards for the 2011-2012 school year. This dataset is provided by the city of Chicago's Data Portal.
 
**3. Chicago Crime Data** : https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days.
    
# Data Analysis Using Python

## House Sales in King County, USA
This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015 :
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv


# Data Visualization And Dashboards Using Excel And Cognos

## Automotive Industry Sample Data
The dataset used in this lab is https://accelerator.ca.analytics.ibm.com/bi/?perspective=authoring&pathRef=.public_folders%2FIBM%2BAccelerator%2BCatalog%2FContent%2FDAT00142&id=i22898C2A4DD748F79E0FC2BD017F4FE8&objRef=i22898C2A4DD748F79E0FC2BD017F4FE8&action=run&format=HTML&cmPropStr=%7B%22id%22%3A%22i22898C2A4DD748F79E0FC2BD017F4FE8%22%2C%22type%22%3A%22reportView%22%2C%22defaultName%22%3A%22DAT00142%22%2C%22permissions%22%3A%5B%22execute%22%2C%22read%22%2C%22traverse%22%5D%7D.

## Scenario
As a regional manager for a chain of car dealerships, you need to build out a dashboard to allow you to understand your sales and service departments.

### Tasks to perform:
* Create two dashboards as follows:

  * One dashboard using the tabbed template that has 4 small rectangles at the top and a large rectangle below - rename this dashboard tab to Sales.
  * One dashboard using the 2 x 2 rectangle areas tabbed template - rename this dashboard tab to Service.

* Capture the following KPI metrics as visualizations:

  * On the Sales dashboard, capture the following KPI metrics:
    
    * In the first small rectangle (Panel 1), capture Profit (formatted to 1 decimal place in millions of US dollars)
    * In the second small rectangle (Panel 2), capture Quantity sold
    * In the third small rectangle (Panel 3), capture the Quantity sold by the model (as a bar chart)
    * In the fourth small rectangle (Panel 4), capture the Average quantity sold
      
* On the Sales dashboard in the large rectangle (Panel 5), display Profit by Dealer ID as a column chart, sorted in ascending order.
* On the Service dashboard, capture the following KPI metrics as visualizations:
  
    * In the top left area (Panel 1), capture the number of recalls per model of car (as a column chart)
    * In the top right area (Panel 2), capture the customer sentiment by comparing positive, neutral, and negative reviews (as a treemap)
    * In the bottom left area (Panel 3), capture the number of cars sold per month compared to the profit (as a line and column chart).
    * In the bottom right area (Panel 4), capture the number of recalls by model and affected system (as a heat map). This will help us understand if there are any outliers for a given model or a specific 
    system.


