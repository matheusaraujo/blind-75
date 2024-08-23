#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask

        if a > 0x7FFFFFFF: a = ~(a ^ mask)

        return a

# @lc code=end

