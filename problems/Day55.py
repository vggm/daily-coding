'''
Implement a URL shortener with the following methods:

shorten(url), 
  which shortens the url into a six-character alphanumeric string, 
  such as zLg6wl.
restore(short), 
  which expands the shortened string into the original url. 
  If no such shortened string exists, return null.
  
Hint: What if we enter the same URL twice?
'''

from Solver import TestSolver

urls = {}

def shorten( url: str ) -> int:
  
  tiny_url = hash( url ) % 10**6
  
  if urls.get(tiny_url) is None:
    urls[tiny_url] = url
  
  return tiny_url    

def restore( tiny_url: int ) -> str | None:
  return urls.get(tiny_url)

if __name__ == '__main__':
  
  solver = TestSolver(False)
  
  url = 'www.google.com'
  shorten_url = shorten(url)
  solver.solve( shorten, url, expected=shorten_url )
  
  solver.solve( restore, shorten_url, expected=url )
  
  solver.show_tests()
