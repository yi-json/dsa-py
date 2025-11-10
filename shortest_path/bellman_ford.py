"""
Implement Bellman-Ford shortest path algorithm.

Given a weighted, directed graph (which may contain negative weights),
and a starting vertex, return the shortest distance from the starting 
vertex to every vertex in the graph.

If a vertex is unreachable from the source, return -1 for that vertex.

If a negative-weight cycle is reachable from the source, 
raise an Exception or return None to indicate invalid distances.

Input:

n - number of vertices (2 <= n <= 100)
edges - list of (u, v, w) directed edges
src - source vertex (0 <= src < n)

Time Complexity: O(n * m)
    - Relax all m edges up to n - 1 times
Space Complexity: O(n)
    - Distance array of size n
"""

from typing import List
import math

def bellman_ford(n: int, edges: List[List[int]], src: int) -> List[int]:
    dist = [math.inf] * n
    dist[src] = 0

    # Relax all edges |V| - 1 times
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # Detect negative-weight cycles
    for u, v, w in edges:
        if dist[u] != math.inf and dist[u] + w < dist[v]:
            return None

    # Convert unreachable vertices to -1
    return [d if d != math.inf else -1 for d in dist]


# Example usage
print(bellman_ford(4, [(0,1,1),(1,2,2),(2,3,3)], 0))
assert bellman_ford(4, [(0,1,1),(1,2,2),(2,3,3)], 0) == [0, 1, 3, 6]