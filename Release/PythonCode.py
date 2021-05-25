import re
import string

# double a value
def DoubleValue(value):
    return value * 2
      
# Prints a multiplication table for the value times one through 10
def MultiplicationTable(value):
  for i in range(1,11):
    print( '{} X {} = {}'.format(value, i, value * i) )
  return 0


