

from typing import Any
from Solver import TestSolver


class TimeMap:
  
  def __init__( self, _map = {} ) -> None:
    self._map : dict = _map.copy()
    
  def set( self, key: Any, value: Any, time: int ) -> None:
    
    map_value = { time: value }
    
    if key not in self._map:
      self._map[key] = map_value
    
    else: self._map[key].update( map_value )
  
  def get( self, key: Any, time: int ) -> Any | None:
    if key in self._map:
      
      if time in self._map[key]: return self._map[key][time]
      
      for k, v in reversed(self._map[key].items()):
        if time >= k: return v
    
    return None
  

if __name__ == '__main__':
  solver = TestSolver(False)
  
  tmap = TimeMap()
  tmap.set(1,1,0); tmap.set(1,2,2)
  solver.solve(
    tmap.get, 1, 1, expected = 1
  )
  solver.solve(
    tmap.get, 1, 3, expected = 2
  )
  
  tmap = TimeMap()
  tmap.set(1,1,5)
  solver.solve(
    tmap.get, 1, 0, expected = None
  )
  solver.solve(
    tmap.get, 1, 10, expected = 1
  )
  
  tmap = TimeMap()
  tmap.set(1,1,0); tmap.set(1,2,0)
  solver.solve(
    tmap.get, 1, 0, expected = 2 
  )

  solver.show_tests()