#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s, n = sum(nums), len(nums)
        return n * (n + 1) // 2 - s


# @lc code=end

