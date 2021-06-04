"""
2021.06.04
mengfanhui
"""
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# 一个搜索的函数，下面会用到，
def dfs(grid, i, j, row, col):
    # 判断边界，和是否遇到了0
    if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == '0':
        return
    # 把1的都换成0
    grid[i][j] = '0'
    # 1节点的上下左右都搜索
    dfs(grid, i+1, j, row, col)
    dfs(grid, i-1, j, row, col)
    dfs(grid, i, j+1, row, col)
    dfs(grid, i, j-1, row, col)

def numIslands(grid):
    if len(grid) == 0:
        return 0
    row, col = len(grid), len(grid[0])
    count = 0
    for i in range(row):
        for j in range(col):
            # 遍历行列，遇到为1的先加1，然后去搜索他的前后左右
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j, row, col)
    return count

print(numIslands(grid))