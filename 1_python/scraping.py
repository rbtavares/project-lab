#!/usr/bin/python3

# Modules
import requests
from bs4 import BeautifulSoup

# Fetch Webpage
def fetchPage():
    return requests.get("https://www.maisgasolina.com/estatisticas-dos-combustiveis/")

# Get element's inner value
def getInnerValue(element):
    return [c for c in element.contents if isinstance(c, str)][0]

# Extract data from webpage
def extractData():
    soup = BeautifulSoup(fetchPage().text, 'html.parser')
    soup = soup.find("div", {"class": "avgPriceList"})
    soup = soup.find_all('div', recursive=False)[:-2]

    return { getInnerValue(soup[i]): float(getInnerValue(soup[i+1])[1:]) for i in range(0, len(soup)-1, 2) }