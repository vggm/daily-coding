# Daily Coding Problems

[`Day 1`](./problems/Day1.py) | EASY | **Google**

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

***Bonus: Can you do this in one pass?***

***

[`Day 2`](./problems/Day2.py) | HARD | **Uber**

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

***Follow-up: what if you can't use division?***

***

[`Day 3`](./problems/Day3.py) | MEDIUM | **Google**

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:

```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

***

[`Day 4`](./problems/Day4.py) | HARD | **Stripe**

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input ```[3, 4, -1, 1]``` should give ```2```. The input ```[1, 2, 0]``` should give ```3```.

You can modify the input array in-place.

***

[`Day 5`](./problems/Day5.py) | HARD | **Jane Street**

```cons(a, b)``` constructs a ```pair```, and ```car(pair)``` and ```cdr(pair)``` returns the first and last element of that pair. For example, ```car(cons(3, 4))``` returns ```3```, and ```cdr(cons(3, 4))``` returns ```4```.

Given this implementation of cons:

```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement ```car``` and ```cdr```.

***

[`Day 12`](./problems/Day12.py) | HARD | **Amazon**

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

***

[`Day 16`](./problems/Day16.py) | EASY | **Twitter**

You run an e-commerce website and want to record the last ```N order ids``` in a log. Implement a data structure to accomplish this, with the following API:

* ```record(order_id):``` adds the order_id to the log
* ```get_last(i):``` gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

***

[`Day 18`](./problems/Day18.py) | HARD | **Google**

Given an ``array of integers`` and a ``number k``, where **1 <= k <= length** of the array, compute the maximum values of each subarray of length k.

For example, given ``array = [10, 5, 2, 7, 8, 7]`` and ``k = 3``, we should get: ``[10, 7, 8, 8]``, since:

* 10 = max(10, 5, 2)
* 7 = max(5, 2, 7)
* 8 = max(2, 7, 8)
* 8 = max(7, 8, 7)

***Do this in O(n) time and O(k) space.*** You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

***

[`Day 19`](./problems/Day19.py) | MEDIUM | **Facebook**

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

***

[`Day 20`](./problems/Day20.py) | EASY | **Google**

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

***
