'''
Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. 
  The objective is to fill the grid with the constraint that every row, 
  column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver
'''

from Solver import PrintSolver

N = 9 # num of rows or columns

def valid( sudoku: list[list[int]], e: int, opt: int ) -> bool:
  i = e // N
  j = e % N
  
  # check vertically
  for row in range(N):
    if row != i and sudoku[row][j] == opt:
      return False
  
  # check horizontally
  for col in range(N):
    if col != j and sudoku[i][col] == opt:
      return False
    
  # check box
  
  
  

def backtracking( sudoku: list[list[int]], e=0 ) -> bool:
  i = e // N
  j = e % N
  
  if e == N*N+1:
    return True
  
  if sudoku[i][j] == 0:
    return backtracking( sudoku, e + 1 )
  
  for opt in range(1, 11):
    sudoku[i][j] = opt
    
    
  sudoku[i][j] = 0
  return False

def sudoku_solver( sudoku: list[list[int]] ) -> list[list[int]]:
  pass

if __name__ == '__main__':
  
  solver = PrintSolver()
  
  sudoku_easy = [ [2,9,0,0,0,0,0,7,0],
                  [3,0,6,0,0,8,4,0,0],
                  [8,0,0,0,4,0,0,0,2],
                  [0,2,0,0,3,1,0,0,7],
                  [0,0,0,0,8,0,0,0,0],
                  [1,0,0,9,5,0,0,6,0],
                  [7,0,0,0,9,0,0,0,1],
                  [0,0,1,2,0,0,3,0,6],
                  [0,3,0,0,0,0,0,5,9] ]
  
  solver.solve( sudoku_solver, sudoku_easy )
  
  sudoku_hard = [ [1,0,0,0,0,7,0,9,0],
                  [0,3,0,0,2,0,0,0,8],
                  [0,0,9,6,0,0,5,0,0],
                  [0,0,5,3,0,0,9,0,0],
                  [0,1,0,0,8,0,0,0,2],
                  [6,0,0,0,0,4,0,0,0],
                  [3,0,0,0,0,0,0,1,0],
                  [0,4,0,0,0,0,0,0,7],
                  [0,0,7,0,0,0,3,0,0] ]
  
  solver.solve( sudoku_solver, sudoku_hard)