#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hist = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hist:
                return [hist[diff], idx]
            hist[num] = idx

# @lc code=end

