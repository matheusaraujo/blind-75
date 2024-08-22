#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left, right = 0, len(nums) - 1
        result = []

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result.append(mid)
                delta = 1
                while mid - delta >= 0 and nums[mid-delta] == target:
                    result.append(mid-delta)
                    delta += 1
                delta = 1
                while mid + delta < len(nums) and nums[mid+delta] == target:
                    result.append(mid+delta)
                    delta += 1
                result.sort()
                return result
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

# @lc code=end

