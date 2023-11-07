'''
Determine whether a doubly linked list is a palindrome. 
  What if it’s singly linked?

For example, 
  1 -> 4 -> 3 -> 4 -> 1 returns True, 
  while 1 -> 4 returns False.
'''

from Solver import TestSolver

class Node:
  def __init__(self, val=-1, nxt=None) -> None:
    self.val = val
    self.next = nxt
    
class SinglyLinked:
  def __init__(self) -> None:
    self.first = Node()
    self.last = Node()
    self.first.next = self.last
    self.curr : Node
    self.size = 0
  
  def add( self, val: int ) -> None:
    self.size += 1
    if self.first.val == -1:
      self.first.val = val
      self.curr = self.first
      return
    
    self.last.next = Node()
    self.last.val = val
    self.last = self.last.next
  
  def next( self ) -> None:
    if not self.is_last():
      val = self.curr.val
      self.curr = self.curr.next
      
  def get_value( self ) -> int:
    return self.curr.val
  
  def is_last( self ) -> None:
    return self.curr is self.last
    
    
def is_palindrome_v3 ( singly_linked: SinglyLinked ) -> bool:
  
  sequence : str = ''
  
  while not singly_linked.is_last():
    sequence += str(singly_linked.get_value())
    singly_linked.next()
  
  return sequence == sequence[::-1]
    
    
def is_palindrome_v2 ( singly_linked: SinglyLinked ) -> bool:
  
  stack = []
  length = singly_linked.size
  
  if length % 2 == 1: # odd size
  
    for i in range(length):
      value = singly_linked.get_value()
      singly_linked.next()
      
      if i == length // 2: # mid
        continue
      
      if stack and value == stack[-1]:
        stack.pop()
      else:
        stack.append(value)
  
  else: # even size
    
    while not singly_linked.is_last():
      value = singly_linked.get_value()
      if stack and value == stack[-1]:
        stack.pop()
      else:
        stack.append(value)
      singly_linked.next()
    
  return not stack


def is_palindrome ( singly_linked: SinglyLinked ) -> bool:
  
  stack = []
  length = singly_linked.size
  for i in range(length):
    value = singly_linked.get_value()
    singly_linked.next()
    
    if length % 2 == 1 and i == length // 2:
      continue
    
    if stack and value == stack[-1]:
      stack.pop()
    else:
      stack.append(value)
    
  return not stack


if __name__ == '__main__':
  
  solver = TestSolver(False)
  
  ''' Test is_palindrome '''
  l = SinglyLinked()
  l.add(1); l.add(4); l.add(3); l.add(4); l.add(1)
  solver.solve(
    is_palindrome,
    l,
    expected=True
  )
  
  l = SinglyLinked()
  l.add(1); l.add(4)
  solver.solve(
    is_palindrome,
    l,
    expected=False
  )
  
  ''' Test is_palindrome_v2 '''
  l = SinglyLinked()
  l.add(1); l.add(4); l.add(3); l.add(4); l.add(1)
  solver.solve(
    is_palindrome_v2,
    l,
    expected=True
  )
  
  l = SinglyLinked()
  l.add(1); l.add(4)
  solver.solve(
    is_palindrome_v2,
    l,
    expected=False
  )
  
  ''' Test is_palindrome_v3 '''
  l = SinglyLinked()
  l.add(1); l.add(4); l.add(3); l.add(4); l.add(1)
  solver.solve(
    is_palindrome_v3,
    l,
    expected=True
  )
  
  l = SinglyLinked()
  l.add(1); l.add(4)
  solver.solve(
    is_palindrome_v3,
    l,
    expected=False
  )
  
  solver.show_tests()
  