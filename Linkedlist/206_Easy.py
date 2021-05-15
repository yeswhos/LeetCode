# 206. 反转链表
"""
2021.05.15
mengfanhui
"""

head = [1,2,3,4,5]
expectedOutput = [5,4,3,2,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        while (head != None and head.next != None):
            # 存两个数，后面可能这俩位置会变
            dNext = dummy.next
            hNext = head.next
            # 三步蛇
            dummy.next = head.next
            head.next = hNext.next
            hNext.next = dNext
        return dummy.next
