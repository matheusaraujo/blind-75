#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

# @lc code=start
class Solution:
    def encode(self, strs: List[str]) -> str:
        lens = map(lambda s: str(len(s)), strs)
        return ",".join(lens) + "==" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        lens = s.split("==")[0]
        if len(lens) == 0: return []
        i, ans = len(lens) + 2, []

        for l in map(int, lens.split(",")):
            ans.append(s[i:(i+l)])
            i += l

        return ans


# @lc code=end

