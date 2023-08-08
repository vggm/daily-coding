"""
Given a list of numbers and a number k , retum whether any two numbers 
  from the list add up to k
  
For example. given [10, 15, 3, 7] and k of 17 ,
return true since 10 + 7 is 17
Bonus: Can you do this in one pass?
"""

from typing import List


def sum2(sequence: List[int], k: int) -> List[int]:
  
  for i, x in enumerate(sequence):
    for _, y in enumerate(sequence, start=i):
      if x + y == k:
        return [x, y]
  
  return []


def bonus(sequence: List[int], k: int) -> List[int]:
  memo = {}
  
  for index, number in enumerate(sequence):
    if memo.get(k-number) is not None:  
      return [sequence[memo[k-number]], sequence[index]]
    
    memo[number] = index
  
  return []


sol = sum2( [10, 15, 3, 7], 17 )
assert sol ==( [10, 7] or [7, 10] ), f'Expected [10, 7] or [7, 10] but got {sol}' 

sol = bonus( [10, 15, 3, 7], 17 )
assert sol ==( [10, 7] or [7, 10] ), f'Expected [10, 7] or [7, 10] but got {sol}' 
