import heapq # min heap by default

# creating a heap
data = [5, 1, 7, 3, 8]
heapq.heapify(data)
print(data)


# adding an element
print("\nAdding an element: 2")
print("before:", data)
heapq.heappush(data, 2)
print("after:", data)


# removing the smallest element
print("\nRemoving the smallest element")
smallest = heapq.heappop(data)
print("smallest:", smallest)
print("data:", data)

# push and pop in one operation
print("\nPushing and popping in one operation")
data = [2, 3, 7, 5, 8]
smallest = heapq.heappushpop(data, 4)
print(smallest)  # Output: 2
print(data)      # Output: [3, 4, 7, 5, 8]

# n Smallest/largest elements in the iterable
smallest_2 = heapq.nsmallest(2, data)
largest_2 = heapq.nlargest(2, data)
print("\n2 Smallest elements in data:", smallest_2)
print("2 largest elements in data:", largest_2)
