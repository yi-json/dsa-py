from collections import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        visited = set()

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        def dfs(node):
            if node in visited:
                return False
            if len(adj_list[node]) == 0:
                return True
            
            visited.add(node)

            for num in adj_list[node]:
                if not dfs(num):
                    return False
            visited.remove(node)
            adj_list[node] = []
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True