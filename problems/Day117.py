"""
  Given a binary tree, return the level of the tree with minimum sum.
"""

from collections import deque
from Solver import TestSolver


class Node:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right


def min_sum_lvl(root: Node) -> int:
  if not root:
    return -1

  lvl = 1  # first level is 1
  minimum_lvl, minimum_lvl_sum = 1, float('inf')
  nodes_to_process = deque([root])

  while nodes_to_process:
    num_of_nodes = len(nodes_to_process)
    curr_lvl_sum = 0
    for _ in range(num_of_nodes):
      node = nodes_to_process.popleft()
      curr_lvl_sum += node.val
      for child in [node.left, node.right]:
        if child:
          nodes_to_process.append(child)

    if curr_lvl_sum < minimum_lvl_sum:
      minimum_lvl_sum = curr_lvl_sum
      minimum_lvl = lvl

    lvl += 1

  return minimum_lvl


if __name__ == '__main__':
  solver = TestSolver(False)

  t = Node(100, Node(2), Node(3))
  solver.solve(
    min_sum_lvl,
    t,
    expected=2
  )

  t = Node(100, Node(2, Node(1)), Node(5))
  solver.solve(
    min_sum_lvl,
    t,
    expected=3
  )

  t = Node(
    100,
    Node(5, Node(2), Node(7)),
    Node(15, Node(12), Node(20))
  )
  solver.solve(
    min_sum_lvl,
    t,
    expected=2
  )

  solver.show_tests()
