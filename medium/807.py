from typing import List
import numpy as np


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        res = 0
        lineRow, lineCol = list(map(max, grid)), list(map(max, zip(*grid)))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res += min(lineRow[i], lineCol[j]) - grid[i][j]
        return res


grid = [
    [3, 0, 8, 4],
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
]
#print(grid)
#print(list(map(max,zip(*grid))))
#print(*grid)
print(Solution().maxIncreaseKeepingSkyline(grid))
