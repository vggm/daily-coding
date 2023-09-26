'''
A knight's tour is a sequence of moves by a knight on 
  a chessboard such that all squares are visited once.

Given N, 
  write a function to return the number of knight's tours on 
  an N by N chessboard.
'''

from Solver import TestSolver

POSSIBLE_KNIGHT_MOVES = (1, -2), (-1, -2), (2, -1), (-2, -1), (1, 2), (-1, 2), (2, 1), (-2, 1)

def print_board( visited: list[bool], N: int ) -> None:
  print('*' * (N+2))
  for row in visited:
    print('*', end=' ')
    for value in row:
      print(value, end=' ')
    print('*')
  print('*' * (N+2))


def all_knight_tours( N: int, start_pos=[0,0] ) -> int:
  visited = [ [ -1 for _ in range(N) ] for _ in range(N) ]
  visited[start_pos[0]][start_pos[1]] = 1
  return knight_moves( 1, N, visited, start_pos )
  
''' Time Complexity: O(8^N*N) '''
def knight_moves( e: int, N: int, visited: list[int], actual: list[int] ) -> int:
  i, j = actual[0], actual[1]
  temp = 0
  
  if e == N*N:
    print_board(visited, N)
    return 1

  for row, col in POSSIBLE_KNIGHT_MOVES:
    
    if (0 <= i+row < N) and (0 <= j+col < N) and (visited[i+row][j+col] == -1): 
        visited[i+row][j+col] = e
        temp += knight_moves( e+1, N, visited, actual=[i+row, j+col] )
        visited[i+row][j+col] = -1
  
  return temp
    

if __name__ == '__main__':
  
  solver = TestSolver()
  
  ''' More than 5 takes too much time '''
  solver.solve( all_knight_tours, 5, expected=304 )
  