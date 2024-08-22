#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def visitIsland(self, grid: List[List[str]], i: int, j: int, islandNumber: str):
        if i < 0 or i >= len(grid): return
        if j < 0 or j >= len(grid[0]): return
        if grid[i][j] != "1": return
        grid[i][j] = islandNumber

        self.visitIsland(grid, i+1, j, islandNumber)
        self.visitIsland(grid, i-1, j, islandNumber)
        self.visitIsland(grid, i, j+1, islandNumber)
        self.visitIsland(grid, i, j-1, islandNumber)


    def numIslands(self, grid: List[List[str]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    self.visitIsland(grid, i, j, str(ans+2))
                    ans += 1
        return ans


# @lc code=end

