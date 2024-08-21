#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        ans = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                ans = max(ans, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return ans

# @lc code=end

