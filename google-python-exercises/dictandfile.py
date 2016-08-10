#!/usr/bin/python -tt

# Python Dict and File
# https://developers.google.com/edu/python/dict-files

import sys
import codecs

def main():
  # dict = key/value hash table
  empty_dict = {}
  di = {}
  di['a'] = 'apple'
  di['b'] = 'banana'
  di['w'] = 'watermelon'
  print di # {'a': 'apple', 'b': 'banana', 'w': 'watermelon'}
  print di['w'] # 'watermelon'
  di['b'] = 'berry'
  'a' in di # True
  if 'c' in di: print di['c']
  # di['c'] ## don't do this
  di.get('c') # None

  dicti = {'a':'AYE','y':'WHY','b':'BYE'}
  for key in dicti:
    print key # 'a' \ 'y' \ 'b'
  for key in dicti.keys(): # same as above
    print key
  print dicti.keys() # ['a','y','b']
  print dicti.values() # ['AYE','WHY','BYE']
  # sort, loop, 'n' print
  for key in sorted(dicti.keys()):
    print key, dicti[key]
  print dicti.items() # list of (key,val) tuples
  dicti['a'] = 'XAY'
  for k,v in sorted(dicti.items()):
    print k, '->', v
  # pro-tip: use dictionaries whenever possible

  # Dict Formatting
  hashh = {}
  hashh['word'] = 'mice'
  hashh['type'] = 'white'
  hashh['num'] = 42
  s = 'I have %(num)d %(type)s %(word)s!' % hashh
  print s

  # Del
  var = 6
  del var # you have deleted var!
  litmus = [1,2,3,4]
  del litmus[0] # [2,3,4]
  del litmus[-2:] # [2]
  del hashh['num'] # {'type': 'white', 'word': 'mice'}

  # Files
  # open('filename','r/w/a/rU') read/write/append/Universal 
  f = open('foo.txt','rU')
  for line in f:
    print line, # so print doesn't add an extra \n
  f.close()
  # f.readlines() ## whole file into a list of lines
  # f.read() ## whole file in a single string

  f = codecs.open('foo.txt','a','utf-8')
  f.write(u'I can read unicode! ch\u00E0o em!')
  f.close()

  # Files Unicode



if __name__ == '__main__':
  main()