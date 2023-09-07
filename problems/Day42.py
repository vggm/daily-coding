'''
Given a list of integers S and a target number k, 
  write a function that returns a subset of S that adds up to k. 
  If such a subset cannot be made, then return null.

Integers can appear more than once in the list. 
  You may assume all numbers in the list are positive.

For example, 
  given S = [12, 1, 61, 5, 9, 2] and k = 24, 
  return [12, 9, 2, 1] since it sums up to 24.
'''

from Solver import TestSolver


def subset_adds_up( S: list[int], k: int ) -> int:
  return bt(0, k, sorted(S, reverse=True), 0, [])


def bt ( e: int, target: int, 
         S: list[int], total: int, 
         parcial: list[int] ) -> list[int] | None:
  
  for i in range(e, len(S)):
    opt = S[i]
    if total + opt <= target:
      total += opt
      parcial.append(opt)
      
      if total == target:
        return parcial

      res = bt( i+1, target, S, total, parcial )
      if res is not None:
        return res
      
      parcial.pop()
      total -= opt
      
      
if __name__ == '__main__':
  
  solver = TestSolver(False)
  
  solver.solve( subset_adds_up, [12, 1, 61, 5, 9, 2], 24, expected=[12,9,2,1] )
  
  solver.show_tests()
  