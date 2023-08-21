"""
Given a singly linked list and an integer k, 
  remove the kth last element from the list. 
  k is guaranteed to be smaller than the length of the list.

The list is very long, 
  so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

from Solver import TestSolver
from random import randint


class Node:
  def __init__( self, value: int, next=None ) -> None:
    self.val = value
    self.next = next


class SinglyLinkedList:
  def __init__(self) -> None:
    self.head = Node(-1)
  
  def add ( self, value: int ):
    node = Node(value)
    node.next = self.head.next
    self.head.next = node
  
  def head ( self ) -> Node:
    return self.head.next if self.head.next else None


def remove_last_kth_element ( elements: SinglyLinkedList, k: int ) -> int:

  prev_node, target_node, curr_node = None, None, elements.head.next
  
  cont = 0
  while curr_node:
    
    if cont == k:
      target_node = elements.head.next
    
    if cont > k:
      target_node = target_node.next
      
      if cont == k+1:
        prev_node = elements.head.next
      else:
        prev_node = prev_node.next
        
    else:
      cont += 1
      
    curr_node = curr_node.next
    if curr_node is None:
      if prev_node is not None:
        prev_node.next = target_node.next
      else:
        elements.head.next = target_node.next
  
  return target_node.val if target_node is not None else -1
      

if __name__ == '__main__':
  
  solver = TestSolver( False )
  
  elements = SinglyLinkedList()
  for i in range( 10, 0, -1 ):
    elements.add( i )
  
  solver.solve( remove_last_kth_element, elements, 3, expected=7 )
  
  elements = SinglyLinkedList()
  for i in range( 100, 0, -1 ):
    elements.add( i )
  
  solver.solve( remove_last_kth_element, elements, 3, expected=97 )
  
  elements = SinglyLinkedList()
  target = randint(0, 45)
  for i in range( 45, -1, -1 ):
    val = i
    if target == 45-i:
      val = expected = randint(0, 200)
    elements.add( val )
  
  solver.solve( remove_last_kth_element, elements, target, expected=expected )
  
  solver.show_tests()
