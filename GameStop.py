# Project title
print("GameStop Analyzing Historical Stock/Revenue Data")

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

# GME Stock price
gme=yf.Ticker("GME")
gme_data=gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()

# Webscraping:GME revenue
url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data=requests.get(url).text
soup_gme=BeautifulSoup(html_data,"html.parser")
gme_revenue= pd.DataFrame(columns=["Date", "Revenue"])

for row in soup_gme.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Revenue = col[1].text
    gme_revenue = gme_revenue.append({"Date":date, "Revenue":Revenue}, ignore_index=True)
    
 gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
 gme_revenue.dropna(inplace=True)
 gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
 gme_revenue.tail()
 
 # Graph
 make_graph(tesla_data, tesla_revenue, 'Historical Share Price and Revenue of Tesla')
