
class MultipleChildTree:
  def __init__(self, val=0, children:dict={}) -> None:
    self.val = val
    self.children = children.copy()
  
  def __repr__(self) -> str:
    return str(self.val)

  def __getitem__(self, key):
    return self.children[key]
  
  def __setitem__(self, key, value) -> None:
    self.children[key] = value
    
  def __iter__(self):
    for key, value in self.children.items():
      yield (key, value)
  

class BinaryTree:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right
  
  def __repr__(self) -> str:
    return str(self.val)
  
  def __add__(self, value):
    return self.val + value

  def __iter__(self):
    for child in [self.left, self.right]:
      yield child
  
  
class Node:
  def __init__(self, val=0, nxt=None) -> None:
    self.val = val
    self.nxt = nxt


class SinglyLinkedList:
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