"""
TC = SC = O(n + m)
"""

from typing import List


def topologicalSort(n: int, edges: List[List[int]]) -> List[int]:
    adj = {i: [] for i in range(n)}
    for src, dst in edges:
        adj[src].append(dst)

    top_sort = []
    visited = set()
    visiting = set() # nodes being visited in the curr dfs call (used to detect cycles)
    
    def dfs(node):
        if node in visited:
            return True
        if node in visiting:
            return False

        visiting.add(node)
        for nei in adj[node]:
            if not dfs(nei):
                return False
        visiting.remove(node)
        visited.add(node) # node has been completely visited
        top_sort.append(node)
        return True

    for i in range(n):
        if not dfs(i):
            return [] # cycle detected
    top_sort.reverse()
    return top_sort
    

n = 3
edges = [[0, 2], [1, 2]]
print(topologicalSort(n, edges))