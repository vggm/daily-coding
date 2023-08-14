
from abc import abstractmethod, ABC
from time import time


CORRECT = '✅'
FAIL = '❌'


class Solver(ABC):
  
  def __init__(self) -> None:
    self.cases = 1
    self.tests = []
  
  @abstractmethod
  def solve( func, *args, **kwargs ):
    pass
  
class PrintSolver(Solver):
  
  def __init__(self) -> None:
    super().__init__()
  
  def solve( self, func, *args, **kwargs ):
    print(f'### Case {self.cases} ###')
    
    start = time()
    func(*args, **kwargs)
    end = time()
    
    print(f'--> Time {(end - start) * 1000:.3f}ms. <--\n')
    self.cases += 1
    
    
class TestSolver(Solver):
  
  def __init__(self, show=True) -> None:
    super().__init__()
    self.show_prints = show
  
  def solve( self, func, *args, **kwargs ):
    if self.show_prints:
      print(f'### Case {self.cases} ###')
    
    start = time()
    sol = func(*args)
    end = time()
    time_spend = (end - start) * 1000
    
    result = CORRECT if sol == kwargs['expected'] else FAIL
    
    if self.show_prints:
      print(f'{result} {sol}') 
      print(f'--> Time {time_spend:.3f}ms. <--\n')
      
    self.cases += 1
    self.tests.append((result, sol, time_spend))
  
  def show_tests(self):
    print('### All tests ###')
    for result, solution, time_spend in self.tests:
      print(f'{result} {solution} - Time: {time_spend:.3f}ms')
    print('#################')
    