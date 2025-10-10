"""
Implement Dijkstra's shortest path algorithm.

Given a weighted, directed graph, and a starting vertex, 
return the shortest distance from the starting vertex to every vertex in the graph.

Input:

n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.
edges - a list of tuples, each representing a directed edge in the form (u, v, w), 
    where u is the source vertex, v is the destination vertex, and w is the weight of the edge, 
    where (1 <= w <= 10).
src - the source vertex from which to start the algorithm, where (0 <= src < n).

Note: If a vertex is unreachable from the source vertex, 
    the shortest path distance for the unreachable vertex should be -1.
"""
import heapq
from typing import List

def dijkstra(n: int, edges: List[List[int]], src: int) -> List[int]:
    G = {i: [] for i in range(n)}
    for u, v, w in edges:
        G[u].append((v, w))

    heap = [(0, src)]
    dist = [float('inf')] * n
    dist[src] = 0
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        
        for nei, w in G[node]:
            new_dist = d + w
            if new_dist < dist[nei]:
                dist[nei] = new_dist
                heapq.heappush(heap, (new_dist, nei))
    return dist

print(dijkstra(4, [(0,1,1),(1,2,2),(2,3,3)], 0))
assert dijkstra(4, [(0,1,1),(1,2,2),(2,3,3)], 0) == [0, 1, 3, 6]