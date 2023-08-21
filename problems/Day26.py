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
    
  def show( self ):
    curr_node = self.head.next
    while curr_node:
      print(curr_node.val, end='')
      curr_node = curr_node.next
      if curr_node:
        print(' -> ', end='')
    print()


def remove_last_kth_element ( elements: SinglyLinkedList, k: int ) -> int:

  prev_node = target_node = curr_node = elements.head.next
  
  cont = 0
  while curr_node:
      
    if cont > k:
      target_node = target_node.next
      
      if cont > k+1:
        prev_node = prev_node.next
        
    if cont < k + 2:
      cont += 1
      
    curr_node = curr_node.next

  prev_node.next = target_node.next

  return target_node.val
      

if __name__ == '__main__':
  
  solver = TestSolver( True )
  
  elements = SinglyLinkedList()
  for i in range( 10, 0, -1 ):
    elements.add( i )
    
  print('\n### k: 3')
  elements.show()
  solver.solve( remove_last_kth_element, elements, 3, expected=7 )
  elements.show()
  
  elements = SinglyLinkedList()
  for i in range( 100, 0, -1 ):
    elements.add( i )
  
  print('\n### k: 3')
  elements.show()
  solver.solve( remove_last_kth_element, elements, 3, expected=97 )
  elements.show()
  
  elements = SinglyLinkedList()
  target = randint(0, 45)
  for i in range( 45, -1, -1 ):
    val = randint(0, 200)
    if target == 45-i:
      expected = val
    elements.add( val )
  
  print('\n### k:', target)
  elements.show()
  solver.solve( remove_last_kth_element, elements, target, expected=expected )
  elements.show()
  
  solver.show_tests()
