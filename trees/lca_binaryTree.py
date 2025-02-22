class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None

    if root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    return left or right
