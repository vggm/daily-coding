"""
Implement an autocomplete system. 
  That is, given a query string s and a set of all possible query strings, 
  return all strings in the set that have s as a prefix.

For example, given the query string "de" and the set of strings [dog, deer, deal], 
  return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

from typing import List


def solve( prefix: str, strings: List[str] ) -> List[str]:
  prefix_length = len(prefix)
  return [ s for s in strings if s[ :prefix_length ] == prefix ]


if __name__ == '__main__':
  pre1 = 'de'
  case1 = ['dog', 'deer', 'deal']
  sol = ['deer', 'deal']
  s = solve(pre1, case1)
  assert s == sol, f"Expected {sol}, but got {s}"