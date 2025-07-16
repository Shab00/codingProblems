from collections import deque

class TreeNode():
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

root = TreeNode("A")
root.left = TreeNode("B")
root.left.left = TreeNode("D")
root.right = TreeNode("C")
root.right.left = TreeNode("E")
root.right.right = TreeNode("F")
root.right.right.left = TreeNode("G")
