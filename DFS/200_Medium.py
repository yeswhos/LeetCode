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

def dfs(grid, i, j, row, col):
    if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == '0':
        return
    grid[i][j] = '0'
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
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j, row, col)
    return count

print(numIslands(grid))