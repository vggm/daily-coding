'''
You are in an infinite 2D grid 
  where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points 
  and the order in which you need to cover the points. 
  Give the minimum number of steps in which you can achieve it. 
  You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2

It takes 1 step to move from (0, 0) to (1, 1). 
  It takes one more step to move from (1, 1) to (1, 2).
'''

from Solver import TestSolver

DIAGONAL = [(1,1), (-1,-1), (-1,1), (1,-1)]
NON_DIAGONAL = [(0,1),(1,0),(0,-1),(-1,0)]


def is_diagonal ( start_point: tuple[int], end_point: tuple[int] ) -> bool:
  return (start_point[0] != end_point[0]) and (start_point[1] != end_point[1])


def distance ( start_point: tuple[int], end_point: tuple[int] ) -> int:
  return abs(start_point[0] - end_point[0]) + abs(start_point[1] - end_point[1])


def min_option ( start_point: tuple[int], end_point: tuple[int], move_options: list[int] ) -> [int,int]:
  mx, my = move_options[0]
  minimum = distance(start_point=(start_point[0]+mx, start_point[1]+my), end_point=end_point)
  for x, y in move_options[1:]:
    d = distance(start_point=(start_point[0]+x, start_point[1]+y), end_point=end_point)
    if d < minimum:
      mx, my, minimum = x, y, d
    
  return mx, my


def shortest_path ( points: list[tuple[int]] ) -> int:
  
  if not points:
    return 0
  
  steps = 0
  stack_points = points[:]
  
  curr_point = stack_points.pop(0)
  while stack_points:
    next_point = stack_points[0]
    options_to_move = NON_DIAGONAL
    if is_diagonal( start_point=curr_point, end_point=next_point ):
      options_to_move = DIAGONAL
    
    x, y = min_option( start_point=curr_point, end_point=next_point, move_options=options_to_move )
    
    curr_point = (curr_point[0]+x, curr_point[1]+y)
    if curr_point == next_point:
      stack_points.pop(0)
    
    steps += 1

  
  return steps


if __name__ == '__main__':
  
  solver = TestSolver(False)
  
  for sequence, exp in [
    ([(0, 0), (1, 1), (1, 2)], 2),
    ([(0, 0), (1, 2), (2, 3)], 3),
    ([(5, 5)], 0),
    ([(5, 5), (4, 4)], 1),
    ([(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)], 4),
    ([(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0)], 8),
    ([(0, 0), (3, 3), (1, 1), (2, 0), (4, 1)], 8),
    ([(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)], 4),
    ([(0, 0), (1, 1), (0, 2), (1, 3), (0, 4), (1, 5)], 5)
  ]:
  
    solver.solve( shortest_path, sequence, expected=exp )
  
  solver.show_tests()
  