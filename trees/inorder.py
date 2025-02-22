class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(node, l):
    if not node:
        return
    dfs(node.left, l)
    l.append(node.val)
    dfs(node.right, l)