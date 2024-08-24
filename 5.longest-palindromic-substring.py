#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def solve(left, right):
            res = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(res):
                    res = s[left:right+1]
                left, right = left - 1, right + 1
            return res

        for i in range(len(s)):
            res = solve(i, i) # odd length
            if len(res) > len(result): result = res
            res = solve(i, i + 1) # even length
            if len(res) > len(result): result = res

        return result


# @lc code=end

