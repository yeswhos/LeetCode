"""
2021.06.03
mengfanhui
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int):
        res = 0
        # 记录下根结点，并且把根结点放入队列中
        # （广度有限一般都与队列有关，先进先出的关系）
        root = TreeNode()
        q = []
        q.append(root)
        # 层序遍历，一层一层遍历
        while len(q) > 0:
            # 记录这一层遍历完了才进入下一层
            size = len(q)
            while size > 0:
                # 先弹一个本层的节点试试水
                cur = q.pop()
                # 假如是范围内的就加上
                if low <= cur.val <= high:
                    res += cur.val
                # 左右看看有没有子节点，为下一层作准备
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
                size -= 1
        return res