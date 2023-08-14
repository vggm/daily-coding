"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

from Solver import TestSolver


class Node:
  def __init__(self, value: int, next = None, prev = None) -> None:
    self.value = value
    self.next = next
    self.prev = prev


class LinkedList:
  def __init__(self) -> None:
    self.first : Node = None
    self.last = Node(0)
    self.actual : Node = None
    self.length = 0
  
  def goNext(self):
    self.actual = self.actual.next
  
  def goPrev(self):
    self.actual = self.actual.prev
  
  def actualValue(self):
    return self.actual.value

  def insert(self, value: int):
    if self.size() == 0:
      self.first = Node(value, next=self.last)
      self.last.prev = self.first
      self.actual = self.first

    else:
      self.last.prev.next = Node(value, next=self.last, prev=self.last.prev)
      self.last.prev = self.last.prev.next
    
    self.length += 1
    
  def size(self):
    return self.length
    
  def goFirst(self):
    self.actual = self.first
    
  def goLast(self):
    self.actual = self.last.prev
    
  def end(self):
    return self.actual == self.last
    
    
def solve( a: LinkedList, b: LinkedList ) -> int: 
  
  if a.size() != b.size():
    return -1
  
  a.goFirst(); b.goFirst()
  while not a.end() and not b.end():

    if a.actualValue() == b.actualValue():
      return a.actualValue()
    
    a.goNext(); b.goNext()
  
  return -1


if __name__ == '__main__':
  
  Solver = TestSolver(False)
  
  a = LinkedList()
  a.insert(3)
  a.insert(7)
  a.insert(8)
  a.insert(10)
  
  b = LinkedList()
  b.insert(99)
  b.insert(1)
  b.insert(8)
  b.insert(10)
  
  Solver.solve(solve, a, b, expected=8)
  
  a = LinkedList()
  a.insert(3)
  a.insert(10)
  a.insert(8)
  a.insert(4)
  
  b = LinkedList()
  b.insert(99)
  b.insert(1)
  b.insert(3)
  b.insert(10)
  
  Solver.solve(solve, a, b, expected=-1)
  
  a = LinkedList()
  a.insert(3)
  a.insert(7)
  a.insert(8)
  
  b = LinkedList()
  b.insert(99)
  b.insert(1)
  b.insert(8)
  b.insert(10)
  
  Solver.solve(solve, a, b, expected=-1)
  
  Solver.show_tests()