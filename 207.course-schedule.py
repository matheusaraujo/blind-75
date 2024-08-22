#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = (0, [])

        for prerequisite in prerequisites:
            graph[prerequisite[0]][1].append(prerequisite[1])

        def findCycle(node: int):
            if graph[node][0] == -1: return True # begin visited
            if graph[node][0] == 1: return False # fully visited

            graph[node] = (-1, graph[node][1]) # begin visited

            for neighbor in graph[node][1]:
                if findCycle(neighbor):
                    return True

            graph[node] = (1, graph[node][1]) # fully visited

            return False

        for i in range(numCourses):
            if findCycle(i):
                return False

        return True


# @lc code=end

