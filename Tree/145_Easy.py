"""
2021.05.25
mengfanhui
"""

# 给你二叉树的根节点 root ，返回它节点值的 后序 遍历。
# 主要思路就是用递归。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode):
        res = []
        def preOrder(node):
            if node is None:
                return
            preOrder(node.left)
            preOrder(node.right)
            res.append(node.val)
        preOrder(root)
        return res