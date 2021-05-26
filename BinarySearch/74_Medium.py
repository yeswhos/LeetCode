"""
2021.05.26
mengfanhui
"""

# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

# 用二分法，先把二维数组搞成一维数组，这样好找mid数。
# 然后根据一维数据的位置来找对应二维数组的位置，方法是行是index/col，列是index%col

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# 输出：true
class Solution:
    def searchMatrix(self, matrix, target):
        # rol是行，col是列
        row = len(matrix)
        col = len(matrix[0])
        if col == 0 or row == 0:
            return False
        left = 0
        right = row * col - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            element = matrix[mid/col][mid%col]
            if element == target:
                return True
            elif element < target:
                left = mid + 1
            elif element > target:
                right = mid - 1
        return False