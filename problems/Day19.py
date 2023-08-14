"""
A builder is looking to build a row of N houses that can be of K different colors.
  He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column,
  represents the cost to build the nth house with kth color, 
  return the minimum cost which achieves this goal.
"""

from typing import List
from math import inf


COST = 0
SEQUENCE = 1


def bt_no_color_repeat(e: int, N: int, K: int, costs: List[List[int]], valid: List[bool], total: int, colors: str) -> None:
  global solution
  if e == N:
    if total < solution[COST]:
      solution = (total, colors)
  
  else:
    for opt in range(K):
      if valid[opt]:
        valid[opt] = False
        
        bt_no_color_repeat(e+1, N, K, costs, valid, total + costs[e][opt], colors + str(opt))
        
        valid[opt] = True
        
        
def bt_color_repeat(e: int, N: int, K: int, costs: List[List[int]], prev: int, total: int, colors: str) -> None:
  global solution
  if e == N:
    if total < solution[COST]:
      solution = (total, colors)
  
  else:
    for opt in range(K):
      if opt != prev:
        bt_color_repeat(e+1, N, K, costs, opt, total + costs[e][opt], colors + str(opt))
        

if __name__ == '__main__':
  M = [ [1,2,3,4], 
        [1,2,1,0], 
        [6,1,1,5], 
        [2,3,5,5] ]
  
  N = len(M)
  K = len(M[0])
  
  solution = (inf, '')
  bt_no_color_repeat(0, N, K, M, [True for _ in range(K)], 0, '')
  assert solution[COST] == 5, f"Expected 5, but got {solution[COST]}."
  print(solution)
  
  solution = (inf, '')
  bt_color_repeat(0, N, K, M, -1, 0, '')
  assert solution[COST] == 4, f"Expected 4, but got {solution[COST]}."
  print(solution)
  