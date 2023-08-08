"""
cons(a, b) constructs a pair, 
  and car(pair) and cdr(pair) returns the first and last element of that pair. 
  For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
    
Implement car and cdr.
"""

def cons( a, b ):
  def pair( f ):
    return f( a, b )
  return pair


# def car( pair ):
#   def first( a, b ):
#     return a
#   return pair(first)


def car( pair ):
  return pair(lambda a, b: a)


# def cdr( pair ):
#   def second( a, b ):
#     return b
#   return pair(second)


def cdr( pair ):
  return pair(lambda a, b: b)


if __name__ == '__main__':
  
  sol = car( cons( 3, 4 ) )
  answer = '👌' if sol == 3 else '🤦‍♂️'
  print(f'{answer} {sol}')
  
  sol = cdr( cons( 3, 4 ) )
  answer = '👌' if sol == 4 else '🤦‍♂️'
  print(f'{answer} {sol}')
