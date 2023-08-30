'''
The power set of a set is the set of all its subsets. 
  Write a function that, given a set, generates its power set.

For example, 
  given the set {1, 2, 3}, 
  it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

from Solver import PrintSolver


def power_set( given_set: list[int] ) -> None:
  res = [[]]
  bt( 0, given_set, parcial=[], sol=res )
  print(res)
  
  
def bt ( e: int, given_set: list[int], parcial: list[int], sol: list[list[int]] ) -> None:
  
  for index in range(e, len(given_set)):
    parcial.append( given_set[index] )
    sol.append(parcial.copy())
    
    bt( index+1, given_set, parcial, sol )
    
    parcial.pop()
    
  
if __name__ == '__main__':
  
  solver = PrintSolver()
  
  solver.solve( power_set, [1, 2, 3] )
  solver.solve( power_set, [1, 2, 3, 4] )
  