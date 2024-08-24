#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result += self.countPalindromes(s, i, i) # odd length palindromes
            result += self.countPalindromes(s, i, i + 1) # even length palindromes

        return result

    def countPalindromes(self, s, left, right) -> int:
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left, right = left - 1, right + 1
        return res


# @lc code=end

