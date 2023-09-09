'''
Given a array of numbers representing the stock prices 
  of a company in chronological order, 
  write a function that calculates the maximum profit 
  you could have made from buying and selling that stock once. 
  You must buy before you can sell it.

For example, 
  given [9, 11, 8, 5, 7, 10], you should return 5, 
  since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''

from Solver import TestSolver


def max_profit( stock_prices: list[int] ) -> int:
  best_profit = 0
  for index, start in enumerate(stock_prices):
    for end in stock_prices[index+1:]:
      best_profit = max( best_profit, end - start )
  return best_profit


if __name__ == '__main__':
  
  solver = TestSolver(False)
  
  solver.solve( max_profit, [9, 11, 8, 5, 7, 10], expected=5 )
  solver.solve( max_profit, [11, 10, 9], expected=0 )
  solver.solve( max_profit, [2, 11, 8, 5, 7, 10], expected=9 )
  solver.solve( max_profit, [2, 10, 5, 13, 1, 9], expected=11 )
  
  solver.show_tests()
