# Summary of Common Data Structures and Algorithms

## Strings
We denote a string as `s`

### Common String Operations
* `s.split(delimiter)` - O(n)
* `s.replace(str1, str2, k)` - O(n*k) or O(n) if k is omitted
    * replaces the first `k` instances of `str2` as `str1`
    * Note: Since Python strings are immutable, we can delete substrings by doing `s.replace(str1, "", n)`

## Lists
Let `l` be a list and `k` be an integer

### Slicing
* `l[:k]` = start at index `k` and go to the end
* `l[-k:]` = start from the `k`-th to last element and go to the end

### Iterating a list backwards
```py
n = len(nums)
for i in range(n - 1, -1, -1):
    print(nums[i])
```

## Lambda Functions
### Using a lambda function on `Counter` object, sorting based on frequency in descending order
```py
    cnt = Counter(nums)
    sorted_cnt = sorted(cnt.items(), key=lambda x : x[1], reverse=True) 
```

## Queues/Deques
```py
# Create a deque
dq = deque([1, 2, 3])  # Initialize with a list
dq = deque()  # Create an empty deque

dq.append(4)  # deque becomes [1, 2, 3, 4]
dq.appendleft(0)  # deque becomes [0, 1, 2, 3, 4]

# Remove from the right (end)
dq.pop()  # Removes 4; deque becomes [0, 1, 2, 3]

# Remove from the left (front)
dq.popleft()  # Removes 0; deque becomes [1, 2, 3]

front = dq[0]  # Access the first element (1)
end = dq[-1]   # Access the last element (3)
```


## Stacks
```py
stack = []
stack.append(element)

# Removes and returns top element
top = stack.pop()

# Accesses the top element without popping it
top = stack[-1]

# checking if stack is empty
if not stack:
	...
```


## Binary Search
### `bisect_right(sorted_list, x)`
Gives you the index where `x` would be inserted, to the right of any equal elements

Suppose we work with tuples:
- `bisect_right(history, (0, 0))` -> Gives the first `(0, ...)` value
- `bisect_right(history, (0, float('inf')))` -> Gives the last `(0, ...)` value



## Trees
### Common Terminology
* rank - position in an in-order traversal
* diameter - length of the longest path between any two nodes in a tree. may or may not pass through the root.

### Lowest Common Ancestor
Defined between two nodes, `p` and `q`, as the lowest node in `T` that has both `p` and `q` as descendants
* Note: A node can be a descendant of itself

If `T` is a binary tree
```py
def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None

    if root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    return left or right
```

### Binary Tree Implementation
```py
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
```

### N-ary Tree Implementation
```py
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
```

### BFS Template - O(n)
```py
from typing import Optional, List
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            level = []
            for i in range(len(q)):
                current = q.popleft()
                level.append(current.val)
                if current.left:
                    q.append(current.left)
                
                if current.right:
                    q.append(current.right)
    
            ans.append(level)
        return ans
```

## Heaps/Priority Queues
### Common Operations + Time Complexities
* insert - O(log n)
* get min/max - O(1)
* extract min/max - O(log n)
* update - O(log n) if we have the index, else O(n)
* build - O(n)

### Common Operations of `heapq` object


* `heapify(iterable)` - O(n)
* `heappush(iterable, x)` - O(log n)
* `heappop(iterable)` - O(log n)
* `heapushpop(iterable, x)` - O(log n)
* `nsmallest(k, iterable, key)` - O(n log k)
* `nlargest(k, iterable, key)` - O(n log k)
    * k: The number of largest elements to return.
    * iterable: The input data we are selecting from.
    * key: A function that determines the value to compare when finding the largest elements.
Example usage: [Top K Largest Elements](https://leetcode.com/problems/top-k-frequent-elements/)
```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        cnt = Counter(nums)
        return heapq.nlargest(k, cnt.keys(), key=cnt.get)
```
* `key=cnt.get` - The `cnt.get` function retrieves the frequency count of each key. `heapq.nlargest()` uses this frequency count to determine the "largest" elements.


### Binary Heap
Typically represented as an array
1. Complete binary tree
    * Every level is completely filled, with the exception of the last row, which is filled from left to right
2. Heap property
    * Min Heap: Each node is less than or equal to its children
    * Max Heap: Each node is greater than or equal to its children

### Useful Info
For a given node at index i, we can find...
* left child: 2*i+1
* right child: 2*i+2
* parent: (i - 1) // 2

### Quickselect Algorithm
Typically used to solve problems that are "find `k` something" such as
* `k`th smallest, `k`th largest, `k`th most frequent, `k`th less frequent

#### Time Complexity
* Average case: O(n)
* Worst case: O(n^2)

1. Select a pivot and form partitions
2. Run the partitioning algorithm only on the side that contains our "top" k-th element

## Bit Manipulation

### XOR Operator - `^`
* Any number XORed with itself cancels out
    * Useful for this problem: [Single Number](https://leetcode.com/problems/single-number/)
* Order of operations does not matter, meaning:


## Miscellaneous

### Collections Data Structures
* `from collections import Counter`
* `from collections import defaultdict`


