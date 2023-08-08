"""
Given the root to a binary tree, implement serialize(root), 
  which serializes the tree into a string, and deserialize(s), 
  which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

SEPARATOR = ','

class Node:
  def __init__(self, val: str, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def serialize( root: Node ) -> str:
  
  if root is None:
    return ''
  
  str_nodes = root.val
  nodes = [root]
  
  while nodes:
    node = nodes.pop(0)
    
    for child in [node.left, node.right]:
      if child is not None and child.val != '':
        nodes.append(child)
        str_nodes += f',{child.val}'
      else:
        str_nodes += f",'None'"
  
  return str_nodes


def deserialize( text: str ) -> Node:
  node_values = text.split(SEPARATOR)
  if len(node_values) == 0:
    return None
  
  dummy = Node('')
  dummy.right = Node(node_values.pop(0))
  nodes = [dummy.right]
  
  while node_values:
    node = nodes.pop(0)
    
    left_val = node_values.pop(0)
    node.left = Node(left_val if left_val != 'None' else '')
    
    right_val = node_values.pop(0)
    node.right= Node(right_val if right_val != 'None' else '')

    nodes.append(node.left)
    nodes.append(node.right)
  
  return dummy.right
  

if __name__ == '__main__':
  node = Node('root', Node('left', Node('left.left')), Node('right'))
  sol = deserialize(serialize(node)).left.left.val
  assert sol == 'left.left', f"Expected 'left.left', but got {sol}."
  
  node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right', Node('right.left'), Node('right.right')))
  sol = deserialize(serialize(node)).right.left.val
  assert sol == 'right.left', f"Expected 'right.left', but got {sol}."