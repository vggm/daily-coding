'''
You have an N by N board. 
    Write a function that, given N, 
    returns the number of possible arrangements 
    of the board where N queens can be placed 
    on the board without threatening each other, 

i.e. no two queens share the same row, 
column, or diagonal.
'''

from Solver import TestSolver


def nqueens( N: int ) -> int:
    queens_combinations = [0]
    bt(0,N,[ -1 for _ in range(N) ],list(range(N)),queens_combinations)
    return queens_combinations[0]


def print_queens( queens: list[int] ) -> None:
    n = len(queens)
    print( '*' * (n+2) )

    for row in range(n):
        print('*', end='')
        for col in range(n):
            v = 'R' if queens[row] == col else ' '
            print( v, end='' )
        print('*')

    print( '*' * (n+2) )


def check_queens( queens: list[int], e: int ) -> bool:
    
    for i in range(e):
        if abs(queens[i] - queens[e]) == abs(i - e):
                return False

    return True


def bt( e: int, n: int, queens: list[int], 
        possible: list[int], 
        sol: list[int] ) -> None:
    
    if e == n:
        print( queens )
        print_queens( queens )
        sol[0] += 1

    else: 
        for i, opt in enumerate(possible):
            queens[e] = opt
            if check_queens(queens, e):
                bt(e+1, n, queens, possible[:i] + possible[i+1:], sol)


if __name__ == '__main__':

    solver = TestSolver()

    solver.solve( nqueens, 1, expected=1 )
    solver.solve( nqueens, 4, expected=2 )
    solver.solve( nqueens, 5, expected=10 )
    solver.solve( nqueens, 8, expected=92 )

    solver.show_tests()
