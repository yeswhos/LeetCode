"""
2021.06.03
mengfanhui
"""
class Node(object):
    def __init__(self, head):
        self.head = head
        self.next = None

def reverse_recursion(head):
    # 递归一个跳出的条件就是找到了最后的节点（先找到最后一个节点）
    if head == None or head.next == None:
        return head
    # p节点代表了该链表最后一个节点，就是递归查找
    p = reverse_recursion(head.next)
    # 找到最后一个节点后，开始把最后一个节点的指针指向倒数第二个，此时head节点应该是倒数第二个节点
    head.next.next = head
    # 倒数第二个节点然后指向空节点，这样下一次循环的时候会认为倒数第二个节点是最后一个。
    head.next = None
    return p