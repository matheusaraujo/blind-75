#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]

        total = 0
        for n in nums:
            total += n
            result = max(result, total)
            total = max(total, 0)

        return result

# @lc code=end

