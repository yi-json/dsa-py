# Summary of Common Data Structures and Algorithms

## Strings
### Common String Operations
We denote a string as `s`
* `s.split(delimiter)` - O(n)
* `s.replace(str1, str2, n)` - O(n)
    * replaces the first `n` instances of `str2` as `str1`
    * Note: Since Python strings are immutable, we can delete substrings by doing `s.replace(str1, "", n)`

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
* `heapify(data)` - O(n)
* `heappush(data, x)` - O(log n)
* `heappop(data)` - O(log n)
* `heapushpop(data, x)` - O(log n)
* `nsmallest(k, data)` - O(n log k)
* `nlargest(k, data)` - O(n log k)


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

### QuickSelect Algorithm

## Miscellaneous

### Collections Data Structures
* `from collections import Counter`
* `from collections import defaultdict`


