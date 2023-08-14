"""
Given an array of integers and a number k, 
  where 1 <= k <= length of the array, 
  compute the maximum values of each subarray of length k.

For example, 
  given array = [10, 5, 2, 7, 8, 7] and k = 3, 
  we should get: [10, 7, 8, 8], 
  since:

  10 = max(10, 5, 2)
  7 = max(5, 2, 7)
  8 = max(2, 7, 8)
  8 = max(7, 8, 7)
  
Do this in O(n) time and O(k) space. 
  You can modify the input array in-place and you do not need to store the results. 
  You can simply print them out as you compute them.

"""

from typing import List
from Solver import PrintSolver


def solve( numbers: List[int], k: int ) -> None:

  for i in range( len(numbers) - k + 1 ):
    print( max( numbers[ i: k+i ] ) )


if __name__ == '__main__':
  solver = PrintSolver()
  solver.solve(solve, [10, 5, 2, 7, 8, 7], 3)
  solver.solve(solve, [10, 3, 5, 1, 8, 4, 9, 12, 3, 4], 4)
  
