"""
2021.06.03
mengfanhui
"""
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# 一个搜索的函数，下面会用到，
def numIslands(grid):
    row, col = len(grid), len(grid[0])
    count = 0
    queue = []
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                count += 1
                queue.append([i, j])
                grid[i][j] = '0'
                while len(queue) > 0:
                    cur = queue.pop()
                    x = cur[0]
                    y = cur[1]
                    if x > 0 and grid[x-1][y] == '1':
                        grid[x-1][j] = '0'
                        queue.append([x-1, y])
                    if y > 0 and grid[x][y-1] == '1':
                        grid[x][y] = '0'
                        queue.append([x, y-1])
                    if x < row-1 and grid[x+1][y] == '1':
                        grid[x+1][y] = '0'
                        queue.append([x+1, y])
                    if y < col-1 and grid[x][y+1] == '1':
                        grid[x][y+1] = '0'
                        queue.append([x, y+1])
    return count

print(numIslands(grid))