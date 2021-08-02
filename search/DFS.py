class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(tree_node):
    if tree_node is not None:
        print(tree_node.val)
        if tree_node.left is not None:
            return dfs(tree_node.left)
        if tree_node.right is not None:
            return dfs(tree_node.right)


if __name__ == '__main__':

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    dfs(root)
