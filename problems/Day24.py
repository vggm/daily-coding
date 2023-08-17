"""
Implement locking in a binary tree. 
  A binary tree node can be locked 
    or unlocked only if all of its descendants 
    or ancestors are not locked.

Design a binary tree node class with the following methods:

* ``is_locked``, which returns whether the node is locked
* ``lock``, which attempts to lock the node. 
  If it cannot be locked, then it should return false.
  Otherwise, it should lock it and return true.
* ``unlock``, 
  which unlocks the node. 
  If it cannot be unlocked, then it should return false. 
  Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers 
  or any other property you would like. 
  You may assume the class is used in a single-threaded program, 
  so there is no need for actual locks or mutexes. 
  Each method ``should run in O(h)``, where h is the height of the tree.
"""

from Solver import TestSolver

class Node:
  
  def __init__( self, 
                locked = False, 
                parent = None, 
                right = None, 
                left = None 
              ) -> None:
    
    self.locked = locked
    self.parent: Node = parent
    self.right: Node = right
    self.left: Node = left  
    
  def __check ( self ) -> bool:
    return all_parents_are_unlocked( self.parent ) or \
      ( all_childs_are_unlocked( self.left ) and all_childs_are_unlocked( self.right ) )
    
  def is_locked ( self ) -> bool:
    return self.locked
  
  def lock ( self ) -> bool:
    if self.is_locked():
      return True
    
    if self.__check():
      self.locked = True
    
    return self.is_locked()
  
  def unlock ( self ) -> bool:
    if not self.is_locked():
      return True
    
    if self.__check():
      self.locked = False
      
    return not self.is_locked()
  

def all_parents_are_unlocked ( node: Node ) -> bool:
  if node is not None:
    if node.is_locked():
      return False

    return all_parents_are_unlocked( node.parent )  
  
  return True


def all_childs_are_unlocked ( root: Node ) -> bool:
  if root is not None:
    if root.is_locked():
      return False
    
    return all_childs_are_unlocked( root.left ) \
      or all_childs_are_unlocked( root.right )
  
  return True
   
  
if __name__ == '__main__':
  
  solver = TestSolver(False)
  
  a = Node()
  
  solver.solve(a.is_locked, expected=False)
  
  b = Node( parent=a )
  c = Node( locked=True, parent=a )
    
  solver.solve(c.is_locked, expected=True)
  
  a.left, a.right = b, c
  
  solver.solve(b.lock, expected=True)
  
  d = Node( parent=c )
  e = Node( locked=True, parent=d )
  d.right = e
  
  solver.solve(d.lock, expected=False)
  
  f = Node( locked=True, parent=b )
  g = Node( parent=f )
  f.right = g
  
  solver.solve(f.unlock, expected=True)
  
  solver.show_tests()
  