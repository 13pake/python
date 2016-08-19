#!/usr/bin/python

# WEB SCRAPER
# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

import sys
# import codecs
import requests
from bs4 import BeautifulSoup

def main():
  
  """
  www.toyota.com
  """
  car_model = 'prius'
  model_year = 2017
  car_id = 1223

  spec_types = ['exterior', 'interior', 'safety_convenience', 'mechanical_performance', 'dimensions', 'weights_capacities', 'tires', 'mpg']

  for spec_type in spec_types:
    url = 'http://www.toyota.com/%s/%d/features/%s/%d' % (car_model, model_year, spec_type, car_id)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # <td class="tcom-datamatrix-subcategory" colspan="4">
    td_subcats = soup.select('td[class="tcom-datamatrix-subcategory"]')
    print '\n' + spec_type.upper()
    for td in td_subcats:
      print td.get_text().strip()
    
    
    # <td data-column-id="1223">
    td_data = soup.select('td[data-column-id="%d"]' % car_id)
    for td in td_data:
      print td.get_text().strip()
    
if __name__ == '__main__':
  main()