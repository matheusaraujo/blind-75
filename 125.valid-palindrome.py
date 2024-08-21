#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        def isValidChar(c: str):
            return c.isalnum()

        while i < j and j >= 0 and i < len(s):
            while i < j and not isValidChar(s[i]):
                i += 1
            while j > i and not isValidChar(s[j]):
                j -= 1

            if s[i].casefold() != s[j].casefold():
                return False
            i, j = i + 1, j - 1

        return True

# @lc code=end

