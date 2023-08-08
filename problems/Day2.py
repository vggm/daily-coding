"""
Given an array of integers, 
  return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 
  the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

from typing import List
from functools import reduce


def solution_day_2( numbers: List[int] ) -> List[int]:
  total = reduce( lambda a, b: a * b, numbers )
  return [ total / number for number in numbers ]


def mul( numbers: List[int], k: int ) -> int:
  total = 1
  for index, number in enumerate(numbers):
    if index == k:
      continue
    
    total *= number
  
  return total
    

def bonus( numbers: List[int] ) -> List[int]:
  return [ mul( numbers, index ) for index in range( len(numbers) ) ]


sol = solution_day_2([1, 2, 3, 4, 5])
assert sol == [120, 60, 40, 30, 24], f"Expected [120, 60, 40, 30, 24], got {sol}"

sol = solution_day_2([3, 2, 1])
assert sol == [2, 3, 6], f"Expected [2, 3, 6], got {sol}"

sol = bonus([1, 2, 3, 4, 5])
assert sol == [120, 60, 40, 30, 24], f"Expected [120, 60, 40, 30, 24], got {sol} / bonus"

sol = bonus([3, 2, 1])
assert sol == [2, 3, 6], f"Expected [2, 3, 6], got {sol} / bonus"