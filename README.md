# Summary of Common Data Structures and Algorithms

## Heaps/Priority Queues
### Common Operations + Time Complexities
* insert - O(log n)
* get min/max - O(1)
* extract min/max - O(log n)
* update - O(log n) if we have the index, else O(n)
* build - O(n)

### Common Operations of `heapq` object
* `heapq.heapify(data)` - O(n)
* `heapq.heappush(data, x)` - O(log n)
* `heapq.heappop(data, x)` - O(log n)
* `heapq.heapushpop(data, x)` - O(log n)
* `heapq.nsmallest(k, data)` - O(n log k)
* `heapq.nlargest(k, data)` - O(n log k)


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
