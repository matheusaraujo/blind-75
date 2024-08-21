#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
          tmp = n1 + n2
          n1 = n2
          n2 = tmp

        return n2

# @lc code=end

