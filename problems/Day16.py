"""
You run an e-commerce website and want to record the last N order ids in a log. 
  Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. 
  i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""

log = []


def record(order_id):
  log.append(order_id)


def get_last(i):
  return log[i-1]


if __name__ == '__main__':
  for i in range(1, 11):
    record(i)

  assert get_last(1) == log[1-1], f"Expected {log[i-1]}, but got {get_last(1)}"