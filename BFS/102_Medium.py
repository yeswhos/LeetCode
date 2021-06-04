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
        # 广度优先都是用的队列，先放根结点
        queue = []
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            # temp记录一层的节点
            temp = []
            while size > 0:
                # 弹出该层节点，然后把值放入temp中
                cur = queue.pop(0)
                temp.append(cur.val)
                # 判断左右的节点放入queue中，在下一次循环中再弹出记录操作啥的
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                size -= 1
            # 这一层temp的节点都放入queue中
            queue.append(temp)
        return queue