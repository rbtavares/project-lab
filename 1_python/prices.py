#!/usr/bin/python3

# Moudles
import os
import time
import json
import requests
from scraping import extractData as scrapeGasPrices

# Constants
CACHE_PATH = './cache/price_data.json'
CACHE_TTL = 60 * 60 * 2 # 2 hours

# Get Gas Prices
def getGasPrices():
    
    # If cache is valid, use cache
    if hasCacheFile():
        
        # Load Cache
        cache_data = loadCache()

        # Check Cache data validity
        if isCacheFileValid(cache_data):
            return loadCache()

    # Scrape gas prices
    price_data = scrapeGasPrices()
    
    # Add timestamp
    price_data = {
        "timestamp": round(time.time()),
        "prices": price_data
    }
    
    # Write data to cache
    writeCache(price_data)

    return price_data

# Check if has cache file
def hasCacheFile():
    return os.path.exists(CACHE_PATH)

# Load cache from file
def loadCache():
    with open(CACHE_PATH, 'r') as fd:
        cache_data = json.load(fd)
    return cache_data

# Check if cache file is valid (timestamp)
def isCacheFileValid(cache_data):
    if 'timestamp' in cache_data:
        return (time.time() - cache_data['timestamp']) < CACHE_TTL
    return False

# Write data to cache file
def writeCache(data):
    with open(CACHE_PATH, 'w') as fd:
        json.dump(data, fd)
    return