#!/urs/bin/python -tt

# Python Regular Expressions
# https://developers.google.com/edu/python/regular-expressions

import sys
import re

def print_match(regex, string):
  match = re.search(regex, string)
  if match:
    print 'Found', match.group()
  else:
    print 'Not found'

def main():
  string = 'I am example word:cat!!!!!!!'
  print_match(r'word:\w\w\w', string)
  # .  = any char except \n
  # \w = [a-zA-Z0-9_]
  # \W = not \w
  # \b = boundary between word and non-word
  # \s = single whitespace char [\n\r\t\f]
  # \s* = all whitespace
  # \S = not \s
  # \t, \n, \r = tab, newline, return
  # \d = decimal digit [0-9]
  # ^  = start of string
  # $  = end of string
  # \  = use in front of . ^ $ * + ? { [ ] \ | ( )
  # +  = 1 or more occurrences, greedy (leftmost & largest)
  # *  = 0 or more occurrences
  # ?  = match 0 or 1 occurrences
  # +?, *? = non-greedy
  # [abc]  = a or b or c
  # [\w.-] = \w or . or - (. is an exception, all other special things work)
  # [a-z]  = [a-z]
  # [abc-] = put the - always at the end
  # [^abc] = not [abc]
  # (a)(bc) = groups into a and bc
  # (?:swag) = not () so (swag)
  # r'([\w.-]+)@([\w.-]+)' = email address w/ username & domain
  string = 'My email is troberts@revacomm.com, yo.'
  match = re.search(r'([\w.-]+)@([\w.-]+)', string)
  print match.group()
  print match.group(1)
  print match.group(2)
  # note: write the regex pattern first, then put parentheses

  # findall
  # Returns list of strings
  string = 'bob.com is email bob@bob.com but the moon is moon@hi.net'
  emails = re.findall(r'[\w.-]+@[\w.-]+', string)
  print emails

  # Using 2 parantheses groups will return list of tuples
  emails = re.findall(r'([\w.-]+)@([\w.-]+)', string)
  print emails

  # re.search(pat,str, re.IGNORECASE) # ignore case...
  # orrrrrrrrrrrrrrrrr re.DOTALL # . matches everything including \n
  #  orrrrrrrrrrrrrrr  re.MULTILINE # allow ^/$ to match each line



if __name__ == '__main__':
  main()