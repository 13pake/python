#!/usr/bin/python

# WEB SCRAPER
# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

import sys
import urllib2
from bs4 import BeautifulSoup

url_path = 'http://www.toyota.com/prius/2017/features/exterior/1223/1224/1225/1226'
page = urllib2.urlopen(url_path)

soup = BeautifulSoup(page, "html.parser") # used 2nd thing to get rid of error

soup.prettify()

print soup.find_all('tr', class_='tcom-datamatrix-row')