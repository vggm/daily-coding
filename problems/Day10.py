"""
Implement a job scheduler which takes in a function f and an integer n, 
  and calls f after n milliseconds.
"""

from time import sleep


def solve( f, n ) -> None:
  sleep( n / 1000 )
  f()
  

def greetings() -> None:
  print("Hello World!")


ms = 3000
print(f"Wating {ms}ms")
solve(greetings, ms)