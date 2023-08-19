"""
Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression 
  and returns whether or not the string matches the regular expression.

For example, 
  given the regular expression "ra." and the string "ray", 
  your function should return true. 
  The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", 
  your function should return true. 
  The same regular expression on the string "chats" should return false.
"""

from Solver import TestSolver


def regex_match ( regex: str, target: str ) -> bool:
  
  memo = {}
  
  def backtracking (i, j) -> bool:
    curr_node = (i,j)
    
    if curr_node in memo:
      return memo[curr_node]
    
    temp = False

    if j >= len(regex) and i >= len(target): # check if we are at the end of the string
      return True 
    
    if j >= len(regex):
      return False
      
    # check if pattern match with the string target
    is_match = i < len(target) and regex[j] in [target[i], '.']
    
    # check if exists kleene closure
    if j + 1 < len(regex) and regex[j+1] == '*': 
      
      # if exists, there is two ways:
      #   0 times
      #   1 or more times      
      temp = (backtracking(i, j+2)                  # dont use the '*' -> 0 times
        or ( is_match and backtracking(i+1, j) ))   # check kleene closure -> 1 or more times
    
    else:
      # doesnt exists kleene closure, so go ahead checking character by character
      temp = is_match and backtracking(i+1, j+1) 
  
    memo[curr_node] = temp
    return temp
  
  return backtracking(0, 0)
  

if __name__ == '__main__':
  
  solver = TestSolver( False )
  
  solver.solve( regex_match, 'ra.', 'ray', expected=True )
  solver.solve( regex_match, 'ra.', 'raymond', expected=False )
  
  solver.solve( regex_match, '.*at', 'chat', expected=True )
  solver.solve( regex_match, '.*at', 'chats', expected=False )
  
  solver.solve( regex_match, 'maa*ri*a', 'maaaaaara', expected=True )

  solver.show_tests()
