#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        tCount, window = {}, {}

        for c in t: tCount[c] = 1 + tCount.get(c, 0)

        have, need = 0, len(tCount)
        res, resLen = [-1, -1], math.inf
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in tCount and window[c] == tCount[c]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    resLen = (right - left + 1)
                    res = [left, right]

                window[s[left]] -= 1
                if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return "" if resLen == math.inf else s[left:right + 1]

# @lc code=end

