#!/usr/bin/python -tt

# Python Sorting
# https://developers.google.com/edu/python/sorting

import sys

def main():
  a = [5, 1, 4, 3]
  sorted(a) # [1, 3, 4, 5]
  # sorted() is better than .sort()

  strs = ['aa', 'BB', 'zz', 'CC']
  sorted(strs)
  # ['BB', 'CC', 'aa', 'zz'] (case sensitive)
  sorted(strs, reverse=True)
  # ['zz', 'aa', 'CC', 'BB']

  # Custom Sorting Wtih key=
  stings = ['tre','eeagdh','af','swag']
  sorted(stings, key=len) # ['af','tre','swag','eeagdh']
  sorted(strs, key=str.lower) # ['aa','BB','CC','zz']
  def my_fn(s):
    return s[-1] # last letter
  stars = ['xc', 'zb', 'yd' ,'wa']
  sorted(stars, key=my_fn) # ['wa', 'zb', 'xc', 'yd']

  # Tuples
  empty_tuple = ()
  tupl = (1, 2, 'hi')
  tupl[2] # 'hi'
  tupl = (1, 2, 'bye') # is okay
  tuplay = ('hi',) # need that awkward comma
  (x,y,z) = ('cow','goes','moo')
  print y # 'goes'
  def Foo():
    return (1,1)
  (cheese,sandwich) = Foo() 
  print Foo()

  # List Comprehensions (optional)
  nums = [1,2,3,4]
  squares = [ n * n for n in nums ] # [1,4,9,16]
  # more on this in the google tutorial

if __name__ == '__main__':
  main()