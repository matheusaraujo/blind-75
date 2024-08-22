#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited, result = {}, []

        def dfs(char):
            if char in visited: return visited[char]

            visited[char] = True # in current path

            for neighbor in adj[char]:
                if dfs(neighbor): return True

            visited[char] = False # fully visited
            result.append(char)

        for char in adj:
            if dfs(char): return ""

        result.reverse()
        return "".join(result)

# @lc code=end

