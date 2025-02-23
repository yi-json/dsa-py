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

## Lambda Functions
### Using a lambda function on `Counter` object, sorting based on frequency in descending order
```py
    cnt = Counter(nums)
    sorted_cnt = sorted(cnt.items(), key=lambda x : x[1], reverse=True)
```

## Trees
### Common Terminology
* rank = position in an in-order traversal

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


## Miscellaneous

### Collections Data Structures
* `from collections import Counter`
* `from collections import defaultdict`


