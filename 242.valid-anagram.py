#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s, set_t = {}, {}

        for i in range(len(s)):
            set_s[s[i]] = set_s.get(s[i], 0) + 1
            set_t[t[i]] = set_t.get(t[i], 0) + 1

        return set_s == set_t

# @lc code=end

