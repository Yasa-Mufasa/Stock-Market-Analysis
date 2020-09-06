'''
Stock Market Analysis - Functions
by Josh Gardner

This file contains the functions to be used in the Stock Market Analysis project.
'''

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime as dt


# This function scrapes the stock data from the list of urls and combines them into a single data frame.
def get_data(url_list=[],Cols=['symbol', 'name', 'price_(intraday)', 'change', 'percent_change', 'volumn', '3_month_avg_vol', 'market_cap', 'pe_ratio']):

    # Creates an empty dataframe to store the scraped data
    dataframes = []

    # scrapes across the urls in the url_list to gather the data using BeautifulSoup
    for url in url_list:
        page = requests.get(url)
        bs = BeautifulSoup(page.content, 'html.parser')
        # We're only interest in the data in the table. We search for the data listed in the table
        tb = bs.find('table')
        # We're only interested in the data labeled with the 'tr' tag in the table.
        rows = tb.find_all('tr')
        cell_data = []
        for row in rows:
            cells = row.find_all('td')
            cells = cells[0:9]
            cell_data.append([cell.text for cell in cells])

        # Here's where we add the data into a DataFrame. However, each individual url results in a different DataFrame.
        dataframes.append(pd.DataFrame(cell_data, columns=Cols).drop(0, axis=0))

    # This is where the different DataFrames are merged together into a single DataFrame.
    final_data = pd.concat(dataframes)
    # Adding a time stamp to the data pull
    final_data['datetime'] = pd.to_datetime(dt.now())
    # This returns the final DataFrame with all data in a single DataFrame
    return final_data


