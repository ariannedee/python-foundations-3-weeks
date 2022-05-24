"""
__name__ is either:
  1. '__main__' if in the current file if run as a script
  2. the dotted path to the file if imported as a module
"""

from things import thing1, thing2

print('In main1.py: __name__ is ' + __name__)
