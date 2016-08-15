#!/usr/bin/python -tt

import sys

def create_wordcount_dict(filename):
  f = open(filename, 'rU')
  wordcount_dict = {}
  for word in f.read().split():
  	word = word.lower()
    if wordcount_dict.get(word) == None: 
      wordcount_dict[word] = 1
    else:
      wordcount_dict[word] += 1
  return wordcount_dict

def main():
  for k,v in create_wordcount_dict('testfile.txt').items():
  	print k, v

if __name__ == '__main__':
  main()