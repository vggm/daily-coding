
from Solver import TestSolver
from typing import List

DISTANCE = 0
PATH = 1

def solve_maze ( map: List[List[bool]], start: tuple, end: tuple ) -> int:
  N = len(map)
  M = len(map[0])
  
  # memo saves as key: a point on the matrix, 
  #             as value a tuple where: 
  #                 0: min distance to the point, 
  #                 1: specific path to the point
  memo = { start: ( 0, str(start) ) }
  
  def backtracking ( start: tuple, curr_path: int, path: str ) -> None:
    y, x = start
    
    for coord_x in [True, False]: # toggle between coord x and coord y
      for opt in [-1, +1]: # x: left right; y: up down

        if coord_x:
          new_x, new_y = x + opt, y 
        else:
          new_x, new_y = x, y + opt
          
        if 0 <= new_x < M and 0 <= new_y < N \
          and not map[new_y][new_x]:
              
          new_coord = ( new_y, new_x )
          prev_path = memo.get( new_coord )
          if prev_path is None: # not prev path
            memo[new_coord] = ( curr_path + 1, path + ' ' + str(new_coord) )
            backtracking( new_coord, curr_path + 1, path + ' ' + str(new_coord) )
          
          else: # if exists a previous path and the new one has a shortest path, replace it
            if curr_path + 1 < prev_path[DISTANCE]:
              memo[new_coord] = ( curr_path + 1, path + ' ' + str(new_coord) )
              backtracking( new_coord, curr_path + 1, path + ' ' + str(new_coord) )

  backtracking( start, 0, str(start) )

  result = memo.get(end)
  if result is not None:
    print(result[PATH])
    return result[DISTANCE]
  
  return -1
    
  
if __name__ == '__main__':
  
  solver = TestSolver()
  
  solver.solve(solve_maze, [
    [False, False, False, False],
    [True,  True,  False, True ],
    [False, False, False, False],
    [False, False, False, False]
  ], (3,0), (0,0), expected = 7)
  
  solver.solve(solve_maze, [
    [False, False, False, False],
    [True,  True,  True,  True ],
    [False, False, False, False],
    [False, False, False, False]
  ], (3,0), (0,0), expected = -1)
  
  solver.solve(solve_maze, [
    [False, True,  False, False, False],
    [False, True,  True,  True,  False],
    [False, True,  False, False, False],
    [False, False, False, True,  False],
    [False, True,  False, True,  False],
    [False, False, False, False, False]
  ], (0,0), (0,4), expected = 10)
  