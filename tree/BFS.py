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

    root = TreeNode(0)
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)
    root.left = node_1
    root.right = node_2
    node_1.left = node_3
    node_1.right = node_4
    node_2.left = node_5
    node_2.right = node_6
    node_3.left = node_7
    node_3.right = node_8
    node_4.left = node_9

    bfs(root)
