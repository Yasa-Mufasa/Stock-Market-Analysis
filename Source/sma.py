'''
Stock Market Analysis
by Josh Gardner

The purpose of this project is to complete a basic analysis of the stock market while gathering the data via web
scraping. The gathered data is from Yahoo Finance, https://finance.yahoo.com.

The first thing to do when web scraping is to check Yahoo's robots.txt file. Yahoo Finance has the following in their
robots.txt file:

    User-agent: *
    Sitemap: https://finance.yahoo.com/sitemap_en-us_desktop_index.xml
    Sitemap: https://finance.yahoo.com/sitemaps/finance-sitemap_index_US_en-US.xml.gz
    Sitemap: https://finance.yahoo.com/sitemaps/finance-sitemap_googlenewsindex_US_en-US.xml.gz
    Disallow: /m/
    Disallow: /r/
    Disallow: /__rapidworker-1.2.js
    Disallow: /__blank
    Disallow: /_td_api
    Disallow: /_remote

This states that for all users, any website extension that does not contain any of the Disallowed web extensions can be
scraped without any issue. This is good news for this project. This project will focus on scrapping data from the three
following websites:

    1. https://finance.yahoo.com/most-active
    2. https://finance.yahoo.com/gainers
    3. https://finance.yahoo.com/losers

To be polite, the initial code developed for this project will not be automated and will only scrap Yahoo Finance when
the code is run. When the code is developed further to include automation, the timing of the web scraping will be set to
not cause any undue stress on Yahoo's servers.

Now that we have checked the robots.txt file for what is allowed, we can focus on building our web scraper. We will be
using BeautifulSoup for our web scraper. The functions we will be using are saved in the sma_funcs.py file.
'''

from sma_funcs import *


# These are the three pages of the most active stocks. This will grab up to 300 stocks.
most_active_urls = ['https://finance.yahoo.com/most-active?count=100&offset=0',
                    'https://finance.yahoo.com/most-active?count=100&offset=100',
                    'https://finance.yahoo.com/most-active?count=100&offset=200']

# These are the three pages of the gainers.
gainers_urls = ['https://finance.yahoo.com/gainers?offset=0&count=100',
                'https://finance.yahoo.com/gainers?count=100&offset=100',
                'https://finance.yahoo.com/gainers?count=200&offset=100']

# These are the three pages of the losers.
losers_urls = ['https://finance.yahoo.com/losers?offset=0&count=100',
               'https://finance.yahoo.com/losers?offset=100&count=100',
               'https://finance.yahoo.com/losers?offset=200&count=100']

# Now let's scrape the data and save the files. These files will be used after the data is pulled over several days.
most_active = get_data(most_active_urls)
print(most_active.head())

gainers = get_data(gainers_urls)
print(gainers.head())

losers = get_data(losers_urls)
print(losers.head())
