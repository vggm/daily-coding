'''
Given an unsorted array of integers, 
  find the length of the longest consecutive elements sequence.

For example, 
  given [100, 4, 200, 1, 3, 2], 
  the longest consecutive element sequence is [1, 2, 3, 4]. 
  Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

from Solver import TestSolver


def longest_consecutive_sequence ( sequence: list[int] ) -> int:
  
  longest = 0
  
  num_set = set(sequence) # instance hash_set
  
  for num in num_set:
    if num - 1 not in num_set: # first element of the consecutive sequence
      currNum = num
      cont = 1
      while currNum + 1 in num_set: # O(1) consult because its a hash_set
        currNum += 1
        cont += 1
      longest = max(longest, cont)
  
  return longest


if __name__ == '__main__':
  solver = TestSolver(False)
  
  solver.solve(
    longest_consecutive_sequence,
    [100, 4, 200, 1, 3, 2],
    expected=4
  )
  
  solver.solve(
    longest_consecutive_sequence,
    [1, 2, 3, 4, 5],
    expected=5
  )
  
  solver.solve(
    longest_consecutive_sequence,
    [10, 20, 30, 40, 50],
    expected=1
  )
  
  solver.solve(
    longest_consecutive_sequence,
    [5, 4, 2, 8, 7, 6, 3, 9, 1],
    expected=9
  )
  
  solver.solve(
    longest_consecutive_sequence,
    [1, 2, 3, 5, 6, 8, 9],
    expected=3
  )
  
  solver.solve(
    longest_consecutive_sequence,
    [],
    expected=0
  )
  
  solver.solve(
    longest_consecutive_sequence,
    [1, 2, 3, 10, 5, 4, 6],
    expected=6
  )
  
  solver.show_tests()