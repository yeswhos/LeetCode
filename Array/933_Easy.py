"""
2021.05.23
mengfanhui
"""

# 写一个 RecentCounter 类来计算特定时间范围内最近的请求。
#
# 请你实现 RecentCounter 类：
#
# RecentCounter() 初始化计数器，请求数为 0 。
# int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
# 保证 每次对 ping 的调用都使用比之前更大的 t 值。
from collections import deque

input = [[],[1],[100],[3001],[3002]]

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        # 队列添加只有append，而且双向队列，pop的时候得popleft来删除最后一个
        self.queue.append(t)
        while len(self.queue) > 1 and t - self.queue[0] > 3000:
            self.queue.popleft()
        return len(self.queue)

obj = RecentCounter()
obj.ping(input)