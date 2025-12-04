from collections import defaultdict, deque
from typing import List

def topologicalSort(n: int, edges: List[List[int]]) -> List[int]:
    in_degrees = [0] * n
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        in_degrees[v] += 1
    
    q = deque([i for i in range(n) if in_degrees[i] == 0])
    ans = []
    while q:
        u = q.popleft()
        ans.append(u)
        
        for v in adj[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                q.append(v)

    if len(ans) != n:
        return []

    return ans