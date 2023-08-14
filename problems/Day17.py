
from typing import List
from Solver import TestSolver

# Each node of the final tree structure
class Node:
  def __init__(self, val: str, *args) -> None:
    self.val = val
    self.next = [*args]
  
  
def string_to_tree( path: str ) -> Node:

  node_lvl = {0: Node('dir')}
  files_path = path.removeprefix(r'dir\n')
  
  for dir in files_path.split(r'\n'):
    curr_lvl = dir.count(r'\t')
    
    node_lvl[curr_lvl - 1].next.append(Node(dir.replace(r'\t', '')))
    node_lvl[curr_lvl] = node_lvl[curr_lvl - 1].next[-1]

  return node_lvl[0]


def longest_path( root: Node, solution: List[list], curr_path: str ) -> None:
  
  if root.val.count('.') != 0: # only files have a dot on its name
    if len(curr_path + root.val) > solution[0][1] :
      solution[0][0] = curr_path + root.val       # longest path
      solution[0][1] = len(curr_path + root.val)  # max length
    return
  
  for node in root.next:
    longest_path(node, solution, curr_path + root.val + '/')


def solve( path: str ) -> list:
  root_dir = string_to_tree( path )
  solution = [ [ '', 0 ] ]
  longest_path( root_dir, solution, '' )
  return solution[0]


if __name__ == '__main__':
  solver = TestSolver(False)
  
  path = r'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'
  solver.solve(solve, path, expected=['dir/subdir2/file.ext', 20]) 
  
  path = r'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
  solver.solve(solve, path, expected=['dir/subdir2/subsubdir2/file2.ext', 32]) 
  
  solver.show_tests()
  