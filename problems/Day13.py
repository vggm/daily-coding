"""
Given an integer k and a string s, 
  find the length of the longest substring 
  that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, 
  the longest substring with k distinct characters is "bcb".
"""

from typing import List
from Solver import TestSolver


def longest_substring ( k: int, s: str ) -> str:
  
  parcial = ''
  sol = ''
  for i, first_char in enumerate(s):
    
    if len(sol) >= len(s[i:]):
      return sol
    
    memo = {}
    parcial = first_char
    memo[first_char] = ''
    
    for c in s[i+1:]:
      
      # Not unique
      if memo.get(c) is not None:
        parcial += c
      
      # Unique
      else:
        if len(memo.keys()) < k:
          memo[c] = ''
          parcial += c
        
        else:
          break
    
    if len(memo.keys()) == k:
      sol = parcial if len(parcial) > len(sol) else sol
  
  return sol


if __name__ == '__main__':
  
  Solver = TestSolver(False)
  
  Solver.solve(longest_substring, 2, 'abcba', expected='bcb')
  Solver.solve(longest_substring, 3, 'abcba', expected='abcba')
  
  Solver.show_tests()
  