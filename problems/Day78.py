
from Day104 import SinglyLinked
from Solver import PrintSolver

def print_singly_linked_list ( sll: SinglyLinked ) -> None:
  
  stack = []
  while not sll.is_last():
    stack.append(sll.get_value())
    sll.next()
    
  print( stack )


def merge_lists ( lists: list[SinglyLinked] ) -> SinglyLinked:
  
  singly_linked_lists = lists[:]
  sorted_singly_linked_list = SinglyLinked()
  while singly_linked_lists:
    min_i = 0
    min_value = singly_linked_lists[0].get_value()
    for index, singly in enumerate(singly_linked_lists[1:], start=1):
      if singly.get_value() < min_value:
        min_value = singly.get_value()
        min_i = index
    
    singly_linked_lists[min_i].next()
    if singly_linked_lists[min_i].is_last():
      singly_linked_lists.pop(min_i)
    
    sorted_singly_linked_list.add(min_value)
    
  print_singly_linked_list(sorted_singly_linked_list)
  return sorted_singly_linked_list


if __name__ == '__main__':
  solver = PrintSolver()
  
  s1,s2,s3 = SinglyLinked(),SinglyLinked(),SinglyLinked()
  s1.add(1);s1.add(3);s1.add(5)
  s2.add(2);s2.add(3);s2.add(4)
  s3.add(1);s3.add(3);s3.add(6)
  
  solver.solve(
    merge_lists,
    [s1,s2,s3]
  )
  