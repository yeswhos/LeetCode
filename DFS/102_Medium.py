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
        res = []
        # 开始深度优先
        def dfs(node, level):
            # 停止条件，节点为空
            if node is None:
                return
            # 假如说没有这一层就加上，比如刚开始长度是1，但传进去是0，就在这个时候就加上一层
            if level > len(res) - 1:
                res.append([])
            # 把元素加进去
            res[level].append(node.val)
            # 递归看左右节点的值，不过就是下一层了
            if node.left is not None:
                dfs(node.left, level+1)
            if node.right is not None:
                dfs(node.right, level+1)
        dfs(root, 0)
        return res
