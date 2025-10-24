import heapq
from typing import List

def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
    adj = {i: [] for i in range(n)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    heap = [(0, 0)] # (weight, vertex) start bfs at v=0
    res = 0 # total weight of MST
    visited = set()

    while heap and len(visited) < n:
        weight, node = heapq.heappop(heap)

        if node in visited:
            continue
        
        visited.add(node)
        res += weight
        for nei, w in adj[node]:
            if nei not in visited:
                heapq.heappush(heap, (w, nei))

    return res if len(visited) == n else -1