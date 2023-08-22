"""
Run-length encoding is a fast and simple method of encoding strings. 
  The basic idea is to represent repeated successive characters as a single count and character. 
  For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
  You can assume the string to be encoded have no digits 
  and consists solely of alphabetic characters. 
  You can assume the string to be decoded is valid.
"""

from Solver import TestSolver


def encode( text: str ) -> str:
  res = ''
  last, count = text[0], 0
  for c in text+'_':
    
    if c != last:
      res += f'{count}{last}'
      count, last = 0, c
    
    count += 1
    
  return res

  
def decode( text: str ) -> str:
  res = ''
  for count, c in zip(text[::2], text[1::2]):
    res += f'{ c * int(count) }'
  return res


def decode_alternative( text: str ) -> str:
  return ''.join( f'{ letter * int(count) }' 
                    for count, letter in zip(text[::2],text[1::2]) )


if __name__ == '__main__':
  
  solver = TestSolver( False )
  
  solver.solve( encode, 'AAAABBBCCDAA', expected='4A3B2C1D2A' )
  solver.solve( decode, '4A3B2C1D2A', expected='AAAABBBCCDAA' )
  
  solver.solve( decode_alternative, '4A3B2C1D2A', expected='AAAABBBCCDAA' )
  
  solver.solve( encode, 'WWEEEEKLLOPPPJHHE', expected='2W4E1K2L1O3P1J2H1E' )
  solver.solve( decode_alternative, '2W4E1K2L1O3P1J2H1E', expected='WWEEEEKLLOPPPJHHE' )
  
  solver.show_tests()
