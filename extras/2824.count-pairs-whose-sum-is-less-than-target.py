#
# @lc app=leetcode id=2824 lang=python3
#
# [2824] Count Pairs Whose Sum is Less than Target
#

# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right, ans = 0, len(nums) - 1, 0

        while left < right:
            if nums[left] + nums[right] < target:
                ans += right - left
                left += 1
            else:
                right -= 1

        return ans


# @lc code=end

