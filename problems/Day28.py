
from typing import List
from Solver import TestSolver


def justify_list ( words: List[str], k: int ) -> List[str]:
  pass


if __name__ == '__main__':
  
  solver = TestSolver()
  
  solver.solve( 
               justify_list, 
               ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
               16,
               expected = [
                 "the  quick brown",
                 "fox  jumps  over",
                 "the   lazy   dog"] )
  