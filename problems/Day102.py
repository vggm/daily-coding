'''
Given a list of integers and a number K, 
  return which contiguous elements of the list sum to K.

For example, 
  if the list is [1, 2, 3, 4, 5] 
  and K is 9, then it should return [2, 3, 4], 
  since 2 + 3 + 4 = 9.
'''

from Solver import TestSolver

def contiguous_elements_sum_opt ( nums: list[int], K: int ) -> list[int]:
  
  memo = {}
  current_sum = 0
  start, end = 0, -1
  memo[0] = -1
  for i, n in enumerate(nums):
    current_sum += n
    if memo.get( current_sum - K ) is not None:
      start = memo[ current_sum - K ] + 1
      end = i
      break
    
    memo[current_sum] = i
  
  if end == -1:
    return []
  
  return nums[start:end+1]


def contiguous_elements_sum_opt_v2 ( nums: list[int], K: int ) -> list[int]:
  
  if len(nums) == 0:
    return []
  
  current_sum = 0
  start, end = 0, 0
  for n in nums:
    
    current_sum += n
    end += 1
    
    if current_sum > K:
      current_sum -= nums[start]
      start += 1
      
    if current_sum == K:
      return nums[start:end]
    
  return []


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
    contiguous_elements_sum_opt_v2,
    [1, 2, 3, 4, 5],
    9,
    expected=[2, 3, 4]
  )
  
  solver.show_tests()