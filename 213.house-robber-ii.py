#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob1(nums[1:]), self.rob1(nums[:-1]))

    def rob1(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(rob1 + n, rob2)
            rob1, rob2 = rob2, tmp

        return rob2

# @lc code=end

