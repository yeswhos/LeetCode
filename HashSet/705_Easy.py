"""
2021.05.24
mengfanhui
"""

# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
#
# 实现 MyHashSet 类：
#
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

# 思路就是整一个超大的数组，把几乎所有值都涵盖，然后add就设该索引为T，remove就F，查找的话就返回这个索引的值T或者F
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = [False] * 1000001

    def add(self, key: int) -> None:
        self.hashSet[key] = True

    def remove(self, key: int) -> None:
        self.hashSet[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hashSet[key]



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)