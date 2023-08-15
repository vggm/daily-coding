"""
Given a dictionary of words and a string made up of those words (no spaces), 
  return the original sentence in a list. 
  If there is more than one possible reconstruction, 
  return any of them. If there is no possible reconstruction, 
  then return null.

For example, 
  given the set of words 'quick', 'brown', 'the', 'fox', 
  and the string "thequickbrownfox", 
  you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', 
  and the string "bedbathandbeyond", 
  return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

from typing import Set, List
from Solver import TestSolver

def words_to_sentence ( words: Set[str], sentence: str ) -> List[str]:
  words_dic = { word: '' for word in words }
  
  parcial = ''
  final_sentence = []
  for c in sentence:
    parcial += c
    
    if words_dic.get(parcial) is not None:
      final_sentence.append(parcial)
      parcial = ''
    
  return final_sentence


if __name__ == '__main__':
  
  Solver = TestSolver(False)
  
  Solver.solve(words_to_sentence, {'quick', 'brown', 'the', 'fox'}, "thequickbrownfox", expected=['the', 'quick', 'brown', 'fox'])
  Solver.solve(words_to_sentence, {'bed', 'bath', 'bedbath', 'and', 'beyond'}, "bedbathandbeyond", expected=['bed', 'bath', 'and', 'beyond'] or ['bedbath', 'and', 'beyond'] )
  
  Solver.show_tests()
  