'''
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. 
  If there are no elements in the stack, 
  then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. 
  If there are no elements in the stack, 
  then it should throw an error or return null.

Each method should run in constant time.
'''

from Solver import TestSolver


class Node():
  def __init__(self, val, nxt = None) -> None:
    self.val = val
    self.nxt = nxt

class Stack():
  def __init__(self) -> None:
    self.head = None
    self.maxi = []
    
  def push(self, val) -> None:
    
    if not self.maxi:
      self.maxi.append(val)
    else:
      self.maxi.append( max( val, self.maxi[-1] ) )
    
    new_node = Node(val, self.head)
    self.head = new_node
    
  def pop(self) -> any:
    
    if self.maxi:
      self.maxi.pop()
    
    value = self.head.val
    self.head = self.head.nxt
    return value
  
  def max(self) -> int:
    return self.maxi[-1]
  
  
if __name__ == '__main__':
  
  Solver = TestSolver(False)
  stack = Stack()
  
  stack.push(1)
  Solver.solve( stack.pop, expected=1 )
  
  stack.push(1)
  stack.push(5)
  stack.push(6)
  stack.push(2)
  stack.push(9)
  Solver.solve( stack.max, expected=9 )
  
  stack.pop()
  Solver.solve( stack.max, expected=6 )
  
  Solver.solve( stack.pop, expected=2 )

  Solver.show_tests()
