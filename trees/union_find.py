"""
Design a Disjoint Set (aka Union-Find) class.

Your UnionFind class should support the following operations:
    UnionFind(int n) will initialize a disjoint set of size n.

    int find(int x) will return the root of the component that x belongs to.

    bool isSameComponent(int x, int y) will return whether x and y belong to the same component.

    bool union(int x, int y) will union the components that x and y belong to. 
        If they are already in the same component, return false, otherwise return true.
    
    int getNumComponents() will return the number of components in the disjoint set.
"""

class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        # find the root of x
        if x != self.parent[x]:
            # path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        # connect x and y
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            self.num_components -= 1
            return True
        # not same component
        return False
        

    def getNumComponents(self) -> int:
        return self.num_components

