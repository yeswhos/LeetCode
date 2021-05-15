# 链表的基本操作
"""
2021.05.15
mengfanhui
"""
from collections import deque

linkedList = deque()
# 添加元素（尾插，指定位置插入元素）
# Add Element O(1)
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
print('Add: ', linkedList)
# insert Element O(n)
linkedList.insert(2, 'insert')
print('Insert: ', linkedList)
# Access Element O(n)
print('Access: ', linkedList[1])
# Search Element O(n)
print('Search: ', linkedList.index(1))
# Update Element O(n)
linkedList[3] = 4
print('Update: ', linkedList)
# Remove Element O(n)
linkedList.remove(4)
print('Remove: ', linkedList)
# Length O(1)
print('Length: ', len(linkedList))