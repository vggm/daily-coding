"""
Given an array of integers, 
  find the first missing positive integer in linear time and constant space. 
  In other words, find the lowest positive integer that does not exist in the array. 
  The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


from typing import List


def solution_day4( numbers: List[int] ) -> int:
  
  numbers_set = set( numbers )
  positives_numbers = list( filter( lambda a: a >= 0, numbers_set ) )
  
  if len( positives_numbers ) == 0:
    return 0
  
  elif len( positives_numbers ) == 1:
    return positives_numbers[ 0 ] + 1
  
  for index in range( 1, len( positives_numbers ) ):
    if positives_numbers[ index ] - 1 != positives_numbers[ index-1 ]:
      return positives_numbers[ index-1 ] + 1
  
  return positives_numbers[ index ] + 1


if __name__ == '__main__':
  
  sol = solution_day4( [3, 4, -1, 1] )
  answer = '👌' if sol == 2 else '🤦‍♂️'
  print(f'{answer} {sol}')
  
  sol = solution_day4( [1, 2, 0] )
  answer = '👌' if sol == 3 else '🤦‍♂️'
  print(f'{answer} {sol}')
  
  sol = solution_day4( [4, 2, 1, 3] )
  answer = '👌' if sol == 5 else '🤦‍♂️'
  print(f'{answer} {sol}')

  sol = solution_day4( [] )
  answer = '👌' if sol == 0 else '🤦‍♂️'
  print(f'{answer} {sol}')
  
  sol = solution_day4( [0] )
  answer = '👌' if sol == 1 else '🤦‍♂️'
  print(f'{answer} {sol}')