#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)

        def isBounded():
            return left < right and top < bottom

        while isBounded():
            # right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # down
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if not isBounded(): break

            # left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            # up
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result
# @lc code=end

