"""
Given a list of integers, 
  write a function that returns the largest sum of non-adjacent numbers. 
  Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
  [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

from typing import List


def solve( numbers: List[int] ) -> int:
  num_and_index = [(num, index) for index, num in enumerate(numbers)]
  num_and_index = sorted(num_and_index, key = lambda a: a[0], reverse=True)
  
  indexes = []
  total = 0
  for n, i in num_and_index:
    if i+1 not in indexes and i-1 not in indexes:
      indexes.append(i)
      total += n
  
  return total


if __name__ == '__main__':
  
  nums = [2, 4, 6, 2, 5]
  sol = 13
  s = solve(nums)
  assert s == sol, f"Expected {sol}, but got {s}"
  
  nums = [5, 1, 1, 5]
  sol = 10
  s = solve(nums)
  assert s == sol, f"Expected {sol}, but got {s}"