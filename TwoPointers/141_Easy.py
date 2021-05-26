"""
2021.05.26
mengfanhui
"""

# 给定一个链表，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环，则返回 true 。 否则，返回 false 。

# 思路就是两个指针，属于快慢指针，一个一次前进一格，一个一次前进两格如果某个指针的下个或者下下个是None，就说明到头了，也就说明链表不是环形的
# 假如两个指针相遇了，就说明是环形

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if head == None:
            return False
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None and fast != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
