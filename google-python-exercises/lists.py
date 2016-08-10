#!/usr/bin/python -tt

# Python Lists
# https://developers.google.com/edu/python/lists

import sys

def main():
  colors = ['red', 'blue', 'green']
  colors[0] # 'red'
  colors[1] # 'blue'
  b = colors # does NOT copy the list, just point
  empty_list = []
  y = [1,2]
  z = [3,4]
  x = y + z # [1, 2, 3, 4]

  # FOR and IN
  for color in colors:
    if color == 'red':
      print color
    elif color == 'green':
      print 'I like ' + color 
      # do not add/remove items while iterating
  cool_kids = ['Trevor','Justus','Daisy','Miles','Riley']
  if 'Trevor' in cool_kids:
    print 'You are a cool kid.'
  s = 'string'
  for ch in s: print ch # prints 's\nt\nr\ni\nn\ng\n'

  # Range
  for i in range(10): # 0-9
    x += [i]
  print x
  w = []
  for i in range(2,5): # 2,3,4
    w += [i]
  print w

  # While Loop
  j = 0
  while j < len(x):
    print x[j]
    j += 3 # access every 3rd element

  # List Methods
  # DO NOT return the list, just modify it
  l = [1, 9, 8]
  l.append(4) # [1,9,8,4] (not a new list)
  l.insert(1, 4) # [1,4,9,8]
  l.extend([9, 1]) # [1,9,8,9,1] (same as l + [9,1])
  l.index(8) # 2 (throws ValueError if cannot find a match)
  l.remove(9) # [1,8]
  l.sort() # [1,8,9]
  l.reverse() # [8,9,1]
  l.pop() # returns 8, [1,9]
  l.pop(0) # returns 1, [9,8]

  # List Slices
  ls = ['a','b','c','d']
  ls[1:-1] # ['b','c']
  ls[0:2] = 'z' # ['z','c','d']

if __name__ == '__main__':
  main()  