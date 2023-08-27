'''
Compute the running median of a sequence of numbers. 
  That is, given a stream of numbers, 
  print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, 
  given the sequence [2, 1, 5, 7, 2, 0, 5], 
  your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''

from Solver import PrintSolver

def sorted_position( num: int, numbers: list[int] ) -> int:
  for index, n in enumerate(numbers):
    if num < n:
      return index
  return -1


def median( numbers: list[int] ) -> None:
  sorted_nums = []
  for index, num in enumerate(numbers, start=1):
    
    s = sorted_position(num, numbers)
    if s != -1:
      sorted_nums.insert(s, num)
    else:
      sorted_nums.append(num)
      
    if index % 2 == 1:
      print(sorted_nums[len(sorted_nums)//2])
    else:
      n1 = sorted_nums[len(sorted_nums)//2]
      n2 = sorted_nums[len(sorted_nums)//2 - 1]
      print(str((n1+n2)/2))


if __name__ == '__main__':
  solver = PrintSolver()

  solver.solve( median, [2, 1, 5, 7, 2, 0, 5] )
  