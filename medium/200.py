from typing import List

def countIsland(grid: List[List[str]]) -> int:
    rows = len(grid)
    islands = 0
    if rows == 0: return islands
    columns = len(grid[0])
    visited = [[False] * columns for x in range (rows)]
    def DFS(i,j):
        visited[i][j] = True
        if grid[i][j] == '1':
            if(j-1>=0 and visited[i][j-1] == False): DFS(i, j-1)
            if(i-1>=0 and visited[i-1][j] == False): DFS(i-1, j)
            if(len(grid[i])>j+1 and visited[i][j+1] == False): DFS(i, j+1)
            if(len(grid)>i+1 and visited[i+1][j] == False): DFS(i+1, j)
    for i in range (0, len(grid)):
        for j in range (0, len(grid[i])):
            if grid[i][j] == '1' and visited[i][j] == False:
                islands += 1
                DFS(i,j)
    return islands

print(countIsland([
    ["1","1","1","1"],
    ["0","0","0","1"],
    ["1","0","1","1"],
    ["1","1","1","1"]]))
