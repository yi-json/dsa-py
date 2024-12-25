from collections import deque
from typing import List


def numIslands(grid: List[List[str]]) -> int:
  n, m = len(grid), len(grid[0])
  islands = 0

  def bfs(i, j):
      q = deque([(i, j)])
      grid[i][j] = "0"

      while q:
          x, y = q.popleft()

          for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
              nx, ny = x + dx, y + dy
              if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1":
                  grid[nx][ny] = "0"  # Mark as visited
                  q.append((nx, ny))
  
  for i in range(n):
      for j in range(m):
          if grid[i][j] == "1":
              islands += 1
              bfs(i, j)

  return islands
        




grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid1)) # exp: 1
print(numIslands(grid2)) # exp: 3