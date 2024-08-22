#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        reachesPacific, reachesAtlantic = set(), set()
        result = list()

        def visit(r, c, reachesList, height):
            if (
                (r, c) in reachesList or
                r not in range(0, rows) or
                c not in range(0, cols) or
                heights[r][c] < height
            ):
                return

            reachesList.add((r, c))

            visit(r + 1, c, reachesList, heights[r][c])
            visit(r - 1, c, reachesList, heights[r][c])
            visit(r, c + 1, reachesList, heights[r][c])
            visit(r, c - 1, reachesList, heights[r][c])

        for r in range(rows):
            visit(r, 0, reachesPacific, heights[r][0])
            visit(r, cols - 1, reachesAtlantic, heights[r][cols - 1])

        for c in range(cols):
            visit(0, c, reachesPacific, heights[0][c])
            visit(rows - 1, c, reachesAtlantic, heights[rows - 1][c])

        for r in range(rows):
            for c in range(cols):
                if (r, c) in reachesPacific and (r, c) in reachesAtlantic:
                    result.append((r, c))

        return result


# @lc code=end

