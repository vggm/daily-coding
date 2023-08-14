"""
Given an array of time intervals (start, end) 
  for classroom lectures (possibly overlapping), 
  find the minimum number of rooms required.

For example, 
  given [(30, 75), (0, 50), (60, 150)], 
  you should return 2.
"""

from typing import List
from Solver import TestSolver


START = 0
END = 1


def day21( time_intervals: List[tuple] ) -> int:
  sorted_time_intervals = sorted(time_intervals)
  rooms = []
  
  for interval in sorted_time_intervals:

    enc = False
    for room in rooms:
      if room[-1][START] < interval[START] < room[-1][END] or \
        interval[END] < room[-1][END] < interval[END]:
          continue
      
      room.append(interval); enc = True
    
    if not enc:
      rooms.append([interval])
  
  return len(rooms)


if __name__ == '__main__':

  Solver = TestSolver(False)
  
  Solver.solve(day21, [(30, 75), (0, 50), (60, 150)], expected=2)
  
  Solver.solve(day21, [(30, 75), (0, 20), (80, 150)], expected=1)
  
  Solver.solve(day21, [(30, 75), (0, 50), (25, 150)], expected=3)
  
  Solver.show_tests()
  