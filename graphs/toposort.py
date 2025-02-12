from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj = [[] for i in range(numCourses)]
    in_degree = [0] * numCourses
    for a, b in prerequisites:
        in_degree[a] += 1
        adj[b].append(a)
    output = []

    def dfs(node):
        output.append(node)
        in_degree[node] -= 1
        for num in adj[node]:
            in_degree[num] -= 1
            if in_degree[num] == 0:
                dfs(num)
    
    for i in range(numCourses):
        if in_degree[i] == 0:
            dfs(i)
    
    return output if len(output) == numCourses else []
    
# Test case 2: Multiple prerequisites
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
result = findOrder(numCourses, prerequisites)
print(f"Test 2: {result} (Expected: [0, 1, 2, 3] or [0, 2, 1, 3])")