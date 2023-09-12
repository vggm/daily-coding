'''
Suppose an arithmetic expression is given as a binary tree. 
  Each leaf is an integer and each internal node is one 
  of '+', '-', '*', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
'''

from Solver import TestSolver


class Node():
  def __init__(self, value, left=None, right=None) -> None:
    self.val = value
    self.left = left
    self.right = right


def result_from_tree ( root: Node ) -> int | float:
  if root.val in ['+', '-', '*', '/']:
    return eval(
      str(result_from_tree(root.left)) 
      + root.val +
      str(result_from_tree(root.right)))
  
  return root.val


if __name__ == '__main__':
  
  solver = TestSolver(False)
  
  '''
       *
      / \
     +    +
    / \  / \
   3  2  4  5
  '''
  root = Node( '*', left=Node( '+', left=Node(3), right=Node(2) ), right=Node( '+', left=Node(4), right=Node(5) ) )
  solver.solve( result_from_tree, root, expected=45 )
  
  '''
       *
      / \
     +    /
    / \  / \
   3  2  8  +
           / \
          2   2
  '''
  root = Node( '*', left=Node( '+', left=Node(3), right=Node(2) ), right=Node( '/', left=Node(8), right=Node('+', left=Node(2), right=Node(2)) ) )
  solver.solve( result_from_tree, root, expected=10 )
  
  solver.show_tests()
