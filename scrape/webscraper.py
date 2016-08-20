#!/usr/bin/python

# WEB SCRAPER
# https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

import sys
import requests
import sets
from bs4 import BeautifulSoup

def main():

  # Command line options
  if len(sys.argv) != 7:
    print 'usage: ./webscraper <username> <password> <oldYear> <oldCar> <newYear> <newCar>'
    sys.exit(0)

  """
  staging.toyotahawaii.com
  """
  carmodel = sys.argv[4]
  modelyear = sys.argv[3]
  url = 'http://staging.toyotahawaii.com/compare/%s-%s' % (modelyear, carmodel)
  page = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
  print url
  soup = BeautifulSoup(page.text, "html.parser")

  # Standard / N/A / Optional requires special Javascript calls
  
  # Remove disclaimer spans
  for span in soup.select('span[class="disc"]'):
    span.decompose()
  
  # Get specs
  toyotahawaii_specs = soup.select('th > span[class="speci_name"]')
  old_specs = []
  for spec in toyotahawaii_specs:
    old_specs.append(' '.join(spec.get_text().split()))

  """
  www.toyota.com
  """
  car_model = sys.argv[6]
  model_year = sys.argv[5]
  car_id = 0 # default
  spec_types = ['exterior', 'interior', 'safety_convenience', 'mechanical_performance', 'dimensions', 'weights_capacities', 'tires', 'mpg']
  new_specs = []

  # Loop through pages
  for spec_type in spec_types:
    url = 'http://www.toyota.com/%s/%s/features/%s/%s' % (car_model, model_year, spec_type, car_id)
    page = requests.get(url)
    print url
    soup = BeautifulSoup(page.text, "html.parser")

    # Get specs
    toyota_specs = (soup.select('td[class="tcom-datamatrix-subcategory"]'))
    for spec in toyota_specs:
      new_specs.append(' '.join(spec.get_text().split()))

    """
    # Standard / N/A / Optional
    toyota_values = soup.select('td[data-column-id="%d"]' % car_id)
    sno_values = []
    for value in toyota_values:
      sno_values.append(' '.join(spec.get_text().split()))

  for value in sno_values:
    f.write(value.encode('utf-8') + '\n')
  f.close()
  """

  """
  Actual vs staging
  """
  new_specs = set(new_specs)
  old_specs = set(old_specs)
  newer_specs = new_specs.difference(old_specs)
  older_specs = old_specs.difference(new_specs)

  f = open('%s-vs-%s-%s-features-difference.txt' % (model_year, modelyear, car_model), 'w')
  f.write('\nNEW SPECS\n')
  for spec in newer_specs:
    f.write(spec.encode('utf-8') + '\n\n')
  f.write('\nOLD SPECS\n')
  for spec in older_specs:
    f.write(spec.encode('utf-8') + '\n\n')
  f.close()

if __name__ == '__main__':
  main()
  