#Import requests and beautifulSoup
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#Connect to web page using requests
url = Request("https://finance.yahoo.com/quote/SPY/profile?p=SPY")
html = urlopen(url)

#Use beautifulSoup to parse the web page into a usable format
beautiful_soup_object = BeautifulSoup(html, 'html.parser' )

#Search the parsed web page for a unique identifier or group of identifiers
result = beautiful_soup_object.find("span", {"data-reactid":"39"} )

#Use the results of the search
print(result.get_text())