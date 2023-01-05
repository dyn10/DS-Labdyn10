# Project title
print("TESLA - Analyzing Historical Stock/Revenue Data")

# Libraries
!pip install yfinance==0.1.67
!mamba install bs4==4.10.0 -y
!pip install nbformat==4.2.0
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
  
  # TSLA Stock price
 tsla=yf.Ticker("TSLA")
 tesla_data=tsla.history(period="max")
 tesla_data.reset_index(inplace=True)
 tesla_data.head()
  
  # Webscraping:Tesla revenue
url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data=requests.get(url).text
soup=BeautifulSoup(html_data,"html.parser")
tesla_revenue= pd.DataFrame(columns=["Date", "Revenue"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Revenue = col[1].text
    tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":Revenue}, ignore_index=True)
    
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue.tail()

# Graphs
make_graph(tesla_data, tesla_revenue, 'Historical Share Price and Revenue of Tesla')
