#!/usr/bin/python -tt

# Python Strings
# https://developers.google.com/edu/python/strings

import sys

'''
I like this 
MULTI-LINE
comment better
'''
"""
than this thing.
it's weird.
don't do it.
unless you have 'single' quotes.
fine then.
"""

def main():
  escaped_chars = '\' \" \n \t'
  single_in_double = "I don't mess up!"
  double_in_single = 'I "dont" mess up'
  multi_line_string = """this is a multi-line string 
and I don't know exactly how it works 
but I think this is it"""
  pi = 3.14
  must_use_str = 'the value of pi is ' + str(pi)
  preferred_int_division = 6 // 5 # = 1
  raw_text = r'\'\"\n\t'

  # String Methods (not Functions)
  s = ' CHEESEburger '
  s.lower() # ' cheeseburger '
  s.upper() # ' CHEESEBURGER '
  s.isalpha() # False
  s.isdigit() # False
  s.isspace() # False
  s.strip() # 'CHEESEburger'
  s.startswith(' CHEESE') # True 
  s.endswith('burger ') # True
  s.find('SEbu') # 5
  s.find('hamburger') # -1
  s.replace('CHEESE','HAM') # ' HAMburger '
  s.split('E') # [' CH','','S','burger ']
  s.split() # ['CHEESEburger']
  'e'.join(s.split('E')) # ' CHeeSeburger '

  # String Slices
  s = 'Hello'
  s[1:4] # 'ell'
  s[1:] # 'ello'
  s[:] # 'Hello' use this to copy a string or list
  s[1:100] # 'ello'
  s[-1] # 'o'
  s[-4] # 'e'
  s[:-3]
  s[:2] # 'He' = s[:2]
  s[-3:]
  s[2:] # 'llo' = s[2:]
  # s[:n] + s[n:] == s

  # String %
  text = ('%d is %s of cows who are mooving %fmph' %
    (4, 'number', 50.0)) # parentheses make this work
  
  # i18n Strings (Unicode)
  unicode_string = u'xin ch\u00E0o!' # xin cha`o!

  # If Statement
  num = sys.argv[1]
  if 0 or None or str() or list(): # these all = False
    print 'You have failed'
  elif num == '1' and True:
    print num, '+ 1 = 2. You are learning well!'
  else:
    print num, '+ 1 = 2? riiiight...'





if __name__ == '__main__':
  main()