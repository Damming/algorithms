class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs(root):
    if root is None:
        return
    my_queue = []
    node = root
    my_queue.append(node)
    while my_queue:
        node = my_queue.pop(0)
        print(node.val)
        if node.left is not None:
            my_queue.append(node.left)
        if node.right is not None:
            my_queue.append(node.right)


if __name__ == '__main__':

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    bfs(root)
