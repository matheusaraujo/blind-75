#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        currMin, currMax = 1, 1

        for n in nums:
            tmp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(tmp, n *currMin, n)
            res = max(res, currMax)

        return res

# @lc code=end

