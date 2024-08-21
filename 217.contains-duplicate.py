#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        history = {}
        for num in nums:
            if num in history:
                return True
            history[num] = 1
        return False
# @lc code=end

