# Daily Coding Problems

[`Day 1`](./problems/Day1.py) | EASY | **Google**

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given ``[10, 15, 3, 7]`` and ``k of 17``, return true since ``10 + 7`` is 17.

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

There exists a staircase with ``N steps``, and you can climb up either ``1 or 2 steps at a time``. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

***What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?***

For example, if ``X = {1, 3, 5}``, you could climb 1, 3, or 5 steps at a time.

***

[`Day 13`](./problems/Day13.py) | HARD | **Amazon**

Given an ``integer k`` and a ``string s``, find the length of the longest substring that contains at most k distinct characters.

For example, given ``s = "abcba"`` and ``k = 2``, the longest substring with k distinct characters is ``"bcb"``.

***

[`Day 14`](./problems/Day14.py) | MEDIUM | **Google**

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

***Hint: The basic equation of a circle is x^2 + y^2 = r^2.***

Personally, I had to watch this video:
[¿En qué consiste el Método Montecarlo?](https://www.youtube.com/watch?v=WJjDr67frtM)

***

[`Day 16`](./problems/Day16.py) | EASY | **Twitter**

You run an e-commerce website and want to record the last ```N order ids``` in a log. Implement a data structure to accomplish this, with the following API:

* ```record(order_id):``` adds the order_id to the log
* ```get_last(i):``` gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

***

[`Day 17`](./problems/Day17.py) | HARD | **Google**

Suppose we represent our file system by a string in the following manner:

The string ``"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"`` represents:

``` bash
dir
    subdir1
    subdir2
        file.ext
```

The directory ``dir`` contains an empty sub-directory ``subdir1`` and a sub-directory ``subdir2`` containing a file ``file.ext``.

The string ``"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`` represents:

``` bash
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```

The directory ``dir`` contains two sub-directories ``subdir1`` and ``subdir2``. ``subdir1`` contains a file ``file1.ext`` and an empty second-level sub-directory ``subsubdir1``. ``subdir2`` contains a second-level sub-directory ``subsubdir2`` containing a file ``file2.ext``.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is ``"dir/subdir2/subsubdir2/file2.ext"``, and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

***Note:***

***The name of a file contains at least a period and an extension.***

***The name of a directory or sub-directory will not contain a period.***

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

Do this in ``O(M + N) time`` (where M and N are the lengths of the lists) and ``constant space``.

***

[`Day 21`](./problems/Day21.py) | EASY | **Snapchat**

Given an array of time intervals ``(start, end)`` for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given ``[(30, 75), (0, 50), (60, 150)]``, you should ``return 2``.

***

[`Day 22`](./problems/Day22.py) | MEDIUM | **Microsoft**

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words ``'quick', 'brown', 'the', 'fox'``, and the string ``"thequickbrownfox"``, you should return ``['the', 'quick', 'brown', 'fox']``.

Given the set of words ``'bed', 'bath', 'bedbath', 'and', 'beyond'``, and the string ``"bedbathandbeyond"``, return either ``['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']``.

***

[`Day 23`](./problems/Day23.py) | EASY | **Google**

You are given an ``M by N matrix`` consisting of booleans that represents a board. ``Each True boolean represents a wall.`` ``Each False boolean represents a tile you can walk on.``

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

``` python
[
    [f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]
]
```

and ``start = (3, 0)`` (bottom left) and ``end = (0, 0)`` (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

***
