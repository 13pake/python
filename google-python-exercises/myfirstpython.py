#!/usr/bin/python -tt

# sys = your usual system goods
# re = regular expresions
# os = operating system interface, file system
import sys

"""
Define functions below:
Multi-line comment xswag
Learning Python is cool
"""

def repeat(s, exclaim):
  # Returns s thrice. If exclaim is True, add '!!!'
  result = s * 3
  if exclaim:
    result = result + '!!!'
  return result

# Typically define main() AFTER defining functions
def main():
  this_is_a_variable = True
  if len(sys.argv) >= 2:
    name = sys.argv[1] + ' ' + sys.argv[2]
  else:
    name = Bob
  print 'Herro there', name
  print repeat('hi ', True)
  stringy = "this is a multi-line string \
            "and I don't know exactly how \
            "it works but I think this is it"
  print stringy


if __name__ == '__main__':
  main()

sys.exit(0)
