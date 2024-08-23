#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, num in enumerate(nums):
            if (i > 0 and nums[i - 1] == nums[i]): continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                s = num + nums[left] + nums[right]
                if s == 0:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif s < 0: left += 1
                else: right -= 1

        return ans

# @lc code=end

