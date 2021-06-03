"""
2021.06.03
mengfanhui
"""
class Node(object):
    def __init__(self, head):
        self.head = head
        self.right = None
        self.left = None

def rangeSumBST(root, low, high):
        res = 0
        # 里面一个递归函数，这个解法就是深度优先和递归结合的
        def sumRecursion(root):
            # 条件是当找到空的节点，也就是最后一层子节点的时候
            if root == None:
                return 0
            # 先走左边的深度
            leftSum = sumRecursion(root.left)
            # 然后右边的深度
            rightSum = sumRecursion(root.right)
            res = leftSum + rightSum
            # 判断那些在范围内符合的值才要加到里面
            if low <= root.val <= high:
                res += root.val
            return res
        return sumRecursion(root)
