#!/usr/bin/python

# WEB SCRAPER
# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

import sys
import requests
from bs4 import BeautifulSoup

def main():

  """
  staging.toyotahawaii.com
  """
  car_model = 'prius-liftback'
  model_year = 2016
  url = 'http://staging.toyotahawaii.com/compare/%d-%s' % (model_year, car_model)

  # cmd line authentication and open page
  if len(sys.argv) == 3:
    page = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
  else:
    print 'usage: ./webscraper <username> <password>'
    sys.exit(0)
  soup = BeautifulSoup(page.text, "html.parser")

  """# Standard / N/A / Optional
  for td in soup.td['class']:
    print td
  span_tags = soup.select('td[class="on"] > span')
  for span in span_tags:
    print span.get_text() #.strip()
  """
  
  """
  Select only feature text
  """
  for span in soup.select('span[class="disc"]'):
    span.decompose()
  
  # Get specs
  old_specs = soup.select('span[class="speci_name"]')

  # TODO: make these into lists

  """# Write features to file
  f = open('staging.txt', 'w')
  for spec in specs:
    f.write(spec.get_text().strip().encode('utf-8') + '\n')
  f.close()
  """
  

  """
  www.toyota.com
  """
  car_model = 'prius'
  model_year = 2017
  car_id = 1223
  spec_types = ['exterior', 'interior', 'safety_convenience', 'mechanical_performance', 'dimensions', 'weights_capacities', 'tires', 'mpg']
  new_specs = []

  
  ###f = open('%d.txt' % car_id, 'w')

  for spec_type in spec_types:
    url = 'http://www.toyota.com/%s/%d/features/%s/%d' % (car_model, model_year, spec_type, car_id)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Get specs
    new_specs += soup.select('td[class="tcom-datamatrix-subcategory"]')

    # TODO: make these into lists

    """
    # Standard / N/A / Optional
    # <td data-column-id="1223">
    td_data = soup.select('td[data-column-id="%d"]' % car_id)
    
    for td in td_data:
      f.write(td.get_text().strip().encode('utf-8') + '\n')
    
  f.close()
  """

  """
  actual vs staging
  """

  def clean(string):
    return ' '.join(string.split())

  def comparsion_is_good(a,b):
    if clean(new_specs[a].get_text()) == clean(old_specs[b].get_text()):
      return True
    else:
      return False
  """
  # fail at comparing lol
  f = open('compare.txt', 'w')
  for i in range(len(new_specs)):
    f.write('\t' + new_specs[i].get_text().strip().encode('utf-8') + '\n')
    f.write('nup ' + old_specs[i].get_text().strip().encode('utf-8') + '\n')
  f.close()
  """

  # TODO: Please clean up this madness

  j = 0
  for i in range(len(new_specs)):
    print i,j
    if comparsion_is_good(i,j):
      print 'GOOD:', new_specs[i].get_text().strip()[:60]
    else:
      # while comparison is not true
      k = i
      while not comparsion_is_good(i,j) and i < len(old_specs)-1:
        i += 1
      if comparsion_is_good(i,j): # a skip happened
        for i in range(j,i):
          print 'DNE: ', new_specs[i].get_text().strip()[:60]
        print 'GOOD:', new_specs[i].get_text().strip()[:60]
      else:
        j = i
        print 'BAD: ', new_specs[i].get_text().strip()[:30], 'vs', old_specs[j].get_text().strip()[:30]
      i = k
    j += 1
  

if __name__ == '__main__':
  main()
  