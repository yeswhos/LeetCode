"""
2021.06.03
mengfanhui
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            temp = []
            while size > 0:
                cur = queue.pop(0)
                temp.append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                size -= 1
            queue.append(temp)
        return queue