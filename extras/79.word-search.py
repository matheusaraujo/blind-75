#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, path = len(board), len(board[0]), set()

        def dfs(r, c, i):
            if i == len(word): return True
            if (not r in range(0, rows) or
                not c in range(0, cols) or
                word[i] != board[r][c] or
                (r, c) in path): return False
            path.add((r, c))
            if dfs(r + 1, c, i + 1): return True
            if dfs(r - 1, c, i + 1): return True
            if dfs(r, c + 1, i + 1): return True
            if dfs(r, c - 1, i + 1): return True
            path.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True

        return False


# @lc code=end

