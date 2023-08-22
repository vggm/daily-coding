"""
Given a string of round, curly, 
  and square open and closing brackets, 
  return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", 
  you should return true.

Given the string "([)]" or "((()", you should return false.
"""

from Solver import TestSolver


brackets_pair = {
  '(': ')',
  '[': ']',
  '{': '}'
}


def brackets_well_formed( brackets: str ) -> bool:
  stack = []
  for c in brackets:
    if c in brackets_pair.keys(): # is an open bracket
      stack.append(c)
      continue
      
    if brackets_pair[stack.pop()] != c:
      return False
  
  return len(stack) == 0


if __name__ == '__main__':
  
  solver = TestSolver( False )
  
  solver.solve( brackets_well_formed, '([])[]({})', expected=True )
  
  solver.solve( brackets_well_formed, '([)]', expected=False )
  solver.solve( brackets_well_formed, '((()', expected=False )
  
  solver.show_tests()
