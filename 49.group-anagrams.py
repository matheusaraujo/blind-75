#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for str in strs:
            key = [0] * 26
            for c in str:
                key[ord(c) - ord("a")] += 1
            ans[tuple(key)].append(str)

        return ans.values()

# @lc code=end

