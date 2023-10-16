'''
Given an array of numbers, 
  find the length of the longest increasing subsequence in the array. 
  The subsequence does not necessarily have to be contiguous.

For example, 
  given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
  the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

from Solver import TestSolver

INF = 999999999999


def longest_subsequence(nums: list[int]) -> int:
    solution = [-INF]
    bt(nums, solution)
    return solution[0]


def bt(nums: list[int], sol: list[int], last: int = -INF,  total: int = 0, e=0) -> None:

    for i in range(e, len(nums)):
        opt = nums[i]
        if opt > last:
            sol[0] = max(sol[0], total + 1)
            bt(nums, sol, opt, total + 1, i + 1)


if __name__ == '__main__':

    solver = TestSolver()

    solver.solve(longest_subsequence, [
                 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], expected=6)
