#naive
from typing import List



class Solution:
    #def countNegatives(self, grid: List[List[int]]) -> int:
    #    count = 0
    #    for i in range(len(grid)):
    #        for j in range(len(grid[1])):
    #            if grid[i][j] < 0: count += 1
    #    return count


    def countNegatives(self, grid: List[List[int]]) -> int:
            count = 0
            row = 0
            col = 0
            while row < len(grid):
                print(row, col)
                if col > 0 and grid[row][col-1] < 0: 
                   col -= 1
                elif grid[row][col] < 0:
                    if col == 0: 
                        count += (len(grid) - row) * len(grid[row])
                        break
                    else: 
                        count += len(grid[row])-col
                        row += 1
                elif col != len(grid[row]): 
                    col += 1
                else: 
                    row += 1
                    col -= 1
            return count

grid =[[3,2],[1,0]]

print(Solution().countNegatives(grid))