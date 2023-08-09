"""
There exists a staircase with N steps, 
  and you can climb up either 1 or 2 steps at a time. 
  Given N, 
  write a function that returns the number of unique ways you can climb the staircase. 
  The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, 
  instead of being able to climb 1 or 2 steps at a time, 
  you could climb any number from a set of positive integers X? 
  For example, if X = {1, 3, 5}, 
    you could climb 1, 3, or 5 steps at a time.
"""

from typing import List

"""
  Backtrcking solution: 
  
  Easy to see, easy to implement but really bad solution
    becasue take too much time and computational resources
"""
def backtracking ( N: int, X: List[int], total = 0 ) -> int:
  
  sol = 0
  
  for num in X:
    
    if total + num <= N:
      total += num
      
      if total == N:
        sol += 1
      
      else:
        sol += backtracking( N, X, total )
      
      total -= num

    else: 
      break
  
  return sol

"""
  Recurive solution:
  
  More efficient than backtracking but still being recursive
"""
def recursive( N: int ) -> int:
  
  if N <= 0:
    return 0
  
  if N == 1:
    return 1
  
  return recursive( N-1 ) + recursive( N-2 )

"""
  iteration solution:
  
  Much more efficiente than backtracking and recursive solution,
    now we just need to do the same but with a set (X)
"""
def iteration( N: int ) -> int:
  
  a = 1
  b = 2
  
  for _ in range(N-1):
    a, b = b, a + b

  return a

"""
  Recursive solution:
  
  Same idea as we saw before, its still being recursive and 
    cost too much time and computational resources
"""
def recursive_solution ( N: int, X: List[int] ) -> int:
  
  if N < 0:
    return 0
  
  if N == 0:
    return 1
  
  return sum( recursive_solution( N-x, X ) for x in X )

"""
  Dynamic programming solution:
  
  Most efficient solution that combine dynamic programming and iteration,
    with a cost of O(N * X) time and O(N) space
"""
def solution ( N: int, X: List[int] ) -> int:
  
  memo = [ 0 for _ in range( N+1 ) ]
  memo[0] = 1
  
  for i in range(1, N+1):
    memo[i] += sum(memo[i-x] for x in X if i - x >= 0)
    
  return memo[N]


if __name__ == '__main__':
  
  # sol = backtracking( N=4, X={ 1, 2 } )
  # assert sol == 5, f"Excpected 5, but got {sol}"

  # sol = backtracking( N=4, X={ 1, 3, 5 } )
  # assert sol == 3, f"Excpected 3, but got {sol}"
  
  sol = solution( 4, {1,3,5} )
  assert sol == 3, f"Expected 3, but got {sol}"
  
  sol1 = backtracking( 30, {1,3,5} )
  sol2 = recursive_solution( 30, {1,3,5} )
  sol3 = solution( 30, {1,3,5} )
  assert sol1 == sol2 == sol3, \
    f"Expected {sol1}, but got sol2={sol2} and sol3={sol3}"
  