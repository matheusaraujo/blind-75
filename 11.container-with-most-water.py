#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, ans = 0, len(height) - 1, 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -=1

        return ans


# @lc code=end

