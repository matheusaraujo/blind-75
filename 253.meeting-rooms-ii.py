#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))

        ans, curr = 0, 0

        times.sort(key = lambda t: (t[0], t[1]))

        for t in times:
            curr += t[1]
            ans = max(ans, curr)

        return ans

# @lc code=end

