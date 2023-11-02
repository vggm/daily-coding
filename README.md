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

[`Day 24`](./problems/Day24.py) | MEDIUM | **Google**

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

* ``is_locked``, which returns whether the node is locked
* ``lock``, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
* ``unlock``, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method ``should run in O(h)``, where h is the height of the tree.

***

[`Day 25`](./problems/Day25.py) | HARD | **Facebook**

Implement regular expression matching with the following special characters:

* ``.`` (period) which matches any single character
* ``*`` (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression ``"ra."`` and the string ``"ray"``, your function should ``return true``. The same regular expression on the string ``"raymond"`` should ``return false``.

Given the regular expression ``".*at"`` and the string ``"chat"``, your function should ``return true``. The same regular expression on the string ``"chats"`` should ``return false``.

***

[`Day 26`](./problems/Day26.py) | MEDIUM | **Google**

Given a ``singly linked list`` and an ``integer k``, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

***

[`Day 27`](./problems/Day27.py) | EASY | **Facebook**

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string ``"([])[]({})"``, you should return true.

Given the string ``"([)]"`` or ``"((()"``, you should return false.

***

[`Day 28`](./problems/Day28.py) | MEDIUM | **Palantir**

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ``["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]`` and ``k = 16``, you should return the following:

``` python
["the  quick brown", # 1 extra space on the left
 "fox  jumps  over", # 2 extra spaces distributed evenly
 "the   lazy   dog"] # 4 extra spaces distributed evenly
```

***

[`Day 29`](./problems/Day29.py) | EASY | **Amazon**

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string ``"AAAABBBCCDAA"`` would be encoded as ``"4A3B2C1D2A"``.

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

***

[`Day 33`](./problems/Day33.py) | EASY | **Microsoft**

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

```
2
1.5
2
3.5
2
2
2
```

***

[`Day 37`](./problems/Day37.py) | EASY | **Google**

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set ``{1, 2, 3}``, it should return ``{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}``.

You may also use a list or array to represent a set.

***

[`Day 38`](./problems/Day38.py) | HARD | **Microsoft**

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

***

[`Day 42`](./problems/Day42.py) | HARD | **Google**

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given ``S = [12, 1, 61, 5, 9, 2]`` and ``k = 24``, return ``[12, 9, 2, 1]`` since it sums up to 24.

*** 

[`Day 43`](./problems/Day43.py) | EASY | **Amazon**

Implement a stack that has the following methods:

* push(val), which pushes an element onto the stack
* pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
* max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

***

[`Day 47`](./problems/Day47.py) | EASY | **Facebook**

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, ``given [9, 11, 8, 5, 7, 10]``, you should ``return 5``, since you could buy the stock at 5 dollars and sell it at 10 dollars.

***

[`Day 50`](./problems/Day50.py) | EASY | **Microsoft**

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of ``'+', '−', '∗', or '/'``.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

```
    *
   / \
  +    +
 / \  / \
3  2  4  5
```

You should return 45, as it is (3 + 2) * (4 + 5).

***

[`Day 54`](./problems/Day54.py) | HARD | **Dropbox**

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.

***

[`Day 55`](./problems/Day55.py) | EASY | **Microsoft**

Implement a URL shortener with the following methods:

* ``shorten(url)``, which shortens the url into a six-character alphanumeric string, such as zLg6wl.
* ``restore(short)``, which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?

***

[`Day 64`](./problems/Day64.py) | HARD | **Google**

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.

***

[`Day 75`](./problems/Day75.py) | HARD | **Microsoft**

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array `[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]`, the longest increasing subsequence has `length 6`: it is `0, 2, 6, 9, 11, 15`.

***

[`Day 99`](./problems/Day99.py) | MEDIUM | **Microsoft**

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given `[100, 4, 200, 1, 3, 2]`, the longest consecutive element sequence is `[1, 2, 3, 4]`. Return its length: `4`.

Your algorithm should run in `O(n) complexity`.

***

[`Day 100`](./problems/Day100.py) | HARD | **Google**

You are in an infinite 2D grid where you can move in any of the 8 directions:

```
(x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
```

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

```
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
```

It takes 1 step to move from `(0, 0)` to `(1, 1)`. It takes one more step to move from `(1, 1)` to `(1, 2)`.