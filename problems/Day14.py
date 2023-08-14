"""
The area of a circle is defined as πr^2. 
  Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""

from Solver import PrintSolver
from random import uniform


def monte_carlo_method( attempts: int ) -> None:
  
  inside = 0
  for _ in range(attempts):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    
    if x**2 + y**2 <= 1:
      inside += 1
  
  print( 4 * (inside / attempts) )


if __name__ == '__main__':
  
  Solver = PrintSolver()
  
  Solver.solve(monte_carlo_method, 1000)