#!/usr/bin/python 

# Libraries used for crawling
import mechanicalsoup
from bs4 import BeautifulSoup
import re, pdb

# Function to fetch all the links and the images from the current page
def fetch(url):
    browser = mechanicalsoup.StatefulBrowser()

    browser.open(url)
    contents = browser.get_current_page()
    links = []
    assets = []
    for link in contents.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))

    for link in contents.findAll('a', attrs={'href': re.compile("^https://")}):
        links.append(link.get('href'))

    for asset in contents.findAll('img'):
        assets.append(asset.get('src'))
    browser.close()
    return links, assets

# Function to fetch all the links and the images from the website
def getWebsiteAssets(url):
    fetch_links, fetch_assets = fetch(url)
    all_links = []
    all_assets = []
    all_assets.append(fetch_assets)
    for resource in fetch_links:
        resource_link, resource_assets = fetch(resource)
        all_links.append(resource_link)
        all_assets.append(resource_assets)
    return all_links, all_assets

# Main Function
if __name__ == '__main__':
    print('Please enter the URL to be fetched: ')
    string = input().strip()
    urls_links, urls_assets = getWebsiteAssets(string)