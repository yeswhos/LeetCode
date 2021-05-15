# 203. 移除链表元素
"""
2021.05.15
mengfanhui
"""
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
head = [1,2,6,3,4,5,6]
val = 6
expectedOutput = [1,2,3,4,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while head != None:
            if head.val == val:
                pre.next = head.next
                head = head.next
            else:
                pre = head
                head = head.next
        return dummy.next
