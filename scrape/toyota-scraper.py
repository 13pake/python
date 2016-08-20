#!/usr/bin/python

# TOYOTA SCRAPER

import sys
import requests
from bs4 import BeautifulSoup

def get_credentials():
  return (sys.argv[1], sys.argv[2])

def get_toyota_features(year, model):
  spec_types = ['exterior', 'interior', 'safety_convenience', 'mechanical_performance', 'dimensions', 'weights_capacities', 'tires', 'mpg']
  specs = []
  for spec_type in spec_types:
    url = 'http://www.toyota.com/%s/%s/features/%s' % (model, str(year), spec_type)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    soup_specs = (soup.select('td[class="tcom-datamatrix-subcategory"]'))
    for soup_spec in soup_specs:
      specs.append(' '.join(soup_spec.get_text().split()))
  return set(specs)

def get_toyotahawaii_features(year, model):
  url = 'http://staging.toyotahawaii.com/compare/%s-%s' % (str(year), model)
  page = requests.get(url, auth=get_credentials())
  soup = BeautifulSoup(page.text, "html.parser")
  for span in soup.select('span[class="disc"]'):
    span.decompose()
  soup_specs = soup.select('th > span[class="speci_name"]')
  specs = []
  for soup_spec in soup_specs:
    specs.append(' '.join(soup_spec.get_text().split()))
  return set(specs)

def get_toyota_models(year):
  page = requests.get('http://www.toyota.com/all-vehicles/')
  soup = BeautifulSoup(page.text, "html.parser")
  soupers = soup.select('div[class="tcom-vehicle-card-image"] > a')
  models = []
  for souper in soupers:
    if souper['href'].endswith(str(year)):
      models.append(str(souper['href'].replace(str(year),'').strip('/')))
  """# Get model names
  for span in soup.select('span'):
    span.unwrap()
  soupers = soup.select('div[class="grade"]')
  models = []
  for souper in soupers:
    if souper.get_text().strip().startswith(str(year)):
      models.append(souper.get_text().replace(str(year),'').strip())
  """
  return set(models)

def get_toyotahawaii_models(year):
  page = requests.get('http://staging.toyotahawaii.com', auth=get_credentials())
  soup = BeautifulSoup(page.text, "html.parser")
  soupers = soup.select('a[class="ve-link"]')
  models = []
  for souper in soupers:
    if souper['href'].replace('explore','').replace('/','').startswith(str(year)):
      models.append(str(souper['href'].replace('explore/' + str(year),'').strip('/').strip('-')))
  # TODO check for duplicate model names
  return set(models)

def main():
  if len(sys.argv) != 3:
    print 'usage: ./toyota-scraper <username> <password>'
    sys.exit(0)

  # Set model year
  model_year = 2017

  # Get model year and model names
  toyota_model_names = get_toyota_models(model_year)
  toyotahawaii_model_names = get_toyotahawaii_models(model_year)

  print toyota_model_names
  print toyotahawaii_model_names

  # Create 2 dictionaries (key:value) of (model:features)
  toyota_models = {}
  toyotahawaii_models = {}
  for model_name in toyota_model_names:
    toyota_features = get_toyota_features(model_year, model_name)
    toyota_models[str(model_year) + '-' + model_name] = toyota_features
  for model_name in toyotahawaii_model_names:
    toyotahawaii_features = get_toyotahawaii_features(model_year, model_name)
    toyotahawaii_models[str(model_year) + '-' + model_name] = toyotahawaii_features

  # TODO: Differentiate features

  # Write to file
  """
  f = open('%s-vs-%s-%s-features-difference.txt' % (str(model_year), modelyear, car_model), 'w')
  f.write('\nNEW SPECS\n')
  for spec in newer_specs:
    f.write(spec.encode('utf-8') + '\n\n')
  f.write('\nOLD SPECS\n')
  for spec in older_specs:
    f.write(spec.encode('utf-8') + '\n\n')
  f.close()
  """

if __name__ == '__main__':
  main()
  