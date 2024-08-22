#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for i in range(n):
            adj[i] = []

        for edge in edges:
            s, t = edge[0], edge[1]
            adj[s].append(t)
            adj[t].append(s)

        visited = set()

        def visit(node: int, prev: int):
            if node in visited: return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prev: continue
                if not visit(neighbor, node):
                    return False
            return True

        return visit(0, -1) and len(visited) == n


# @lc code=end

