'''
Given a list of integers and a number K, 
  return which contiguous elements of the list sum to K.

For example, 
  if the list is [1, 2, 3, 4, 5] 
  and K is 9, then it should return [2, 3, 4], 
  since 2 + 3 + 4 = 9.
'''

from Solver import TestSolver

def contiguous_elements_sum ( nums: list[int], K: int ) -> list[int]:
  
  parcial_sum = 0
  for i, n in enumerate(nums[:-1]):
    parcial_sum = n
    for j, n in enumerate(nums[i+1:], start=i+1):
      parcial_sum += n
      if parcial_sum > K:
        break
      
      if parcial_sum == K: # solution found
        return [*nums[i:j+1]]
  
  return [] # solution not found


if __name__ == '__main__':
  
  solver = TestSolver(False)
  
  solver.solve(
    contiguous_elements_sum,
    [1, 2, 3, 4, 5],
    9,
    expected=[2, 3, 4]
  )
  
  solver.show_tests()