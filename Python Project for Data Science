## Python Project for Data Science
# Required Packages
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Using the yfinance Library to Extract Stock Data
 ## Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is TSLA
   Tesla = yf.Ticker("TSLA")
   !wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json

 ## Using the ticker object and the function `history` extract stock information and save it in a dataframe named `tesla_data`. Set the `period` parameter to `max` so we get information for the maximum amount of time.
    Tesla_data = Tesla.history(period="max")

## Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame and display the first five rows of the tesla_data dataframe using the head function
   Tesla_data.reset_index(inplace=True)
   Tesla_data.head()

# Use Webscraping to Extract Tesla Revenue Data
 ## Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response     
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
    data = requests.get(url).text
    from bs4 import BeautifulSoup # this module helps in web scrapping.
    import requests
    Tesla_data = pd.read_html(url, flavor='bs4')
    tesla_rev = Tesla_data[1]
    tesla_rev

    tesla_revenue = tesla_rev.rename(columns={'Tesla Quarterly Revenue(Millions of US $)': 'Date', 'Tesla Quarterly Revenue(Millions of US $).1': 'Revenue'})
    tesla_revenue

# Use yfinance to Extract Stock Data
  ## Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is GME.
    GameStop = yf.Ticker("GME")
    gme_data = GameStop.history(period="max")
    gme_data.reset_index(inplace=True)
    gme_data.head()

# Use Webscraping to Extract GME Revenue Data
 ##  Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named html_data.
    url4 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
    data4 = requests.get(url4).text
    soup = BeautifulSoup(data4, "html5lib")
    print(soup.prettify())

 ## Using BeautifulSoup or the read_html function extract the table with GameStop Revenue and store it into a dataframe named gme_revenue. The dataframe should have columns Date and Revenue. Make sure the comma and dollar sign is removed from the Revenue column
    from bs4 import BeautifulSoup # this module helps in web scrapping.
    import requests
    gme_data = pd.read_html(url4, flavor='bs4')
    gme_temp = gme_data[1]
    gme_temp
   
   from bs4 import BeautifulSoup # this module helps in web scrapping.
   import requests
   gme_revenue = gme_temp.rename(columns={'GameStop Quarterly Revenue(Millions of US $)': 'Date', 'GameStop Quarterly Revenue(Millions of US $).1': 'Revenue'})
   gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
   gme_revenue.dropna(inplace=True)

  gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

 ##  `make_graph` functions takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.

 def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

 ## Graph the GameStop Stock Data, also provide a title for the graph
    make_graph(gme_data, gme_revenue, 'GameStop')

## Graph the Tesla Stock Data
   make_graph(Tesla_data, tesla_revenue, 'Tesla')



 


 
