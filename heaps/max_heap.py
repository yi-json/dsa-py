import heapq

# Original list
data = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Convert to max-heap
max_heap = [-x for x in data]  # Negate the values
heapq.heapify(max_heap)        # Create a heap

# Access elements in max-heap order
while max_heap:
    max_value = -heapq.heappop(max_heap)  # Negate again to restore original value
    print(max_value)