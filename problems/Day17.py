
import re
from typing import List
from Solver import TestSolver


class Node:
  def __init__(self, val, *args) -> None:
    self.val = val
    self.next = [*args]
    
  
def string_to_tree( path: str ) -> Node | None:
  if path[:3] != 'dir':
    return 
  
  dummy = Node('-1')
  curr = Node('dir')
  dummy.next.append(curr)
  
  curr_path = path.removeprefix('dir')
  regex = r'\\n\\t(?!\\t)'
  for dir in re.split( regex, curr_path ):
    print(dir)
  
  


def longest_path( root: Node, solution: List[tuple] ) -> None:
  pass


def solve( path: str ) -> tuple:
  root_dir = string_to_tree( path )
  solution = [ ( '', 0 ) ]
  longest_path( root_dir, solution )
  return solution[0]


if __name__ == '__main__':
  solver = TestSolver(False)
  
  path = r'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'
  solver.solve(solve, path, expected=('dir/subdir2/file.ext', 20)) 
  
  # path = r'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
  # solver.solve(solve, path, expected=('dir/subdir2/subsubdir2/file2.ext', 20)) 
  
  # solver.show_tests()
  