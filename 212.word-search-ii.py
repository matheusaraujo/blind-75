#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        self.refs = 0

    def addWord(self, word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children: curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1
        curr.word = True

    def removeWord(self, word):
        curr = self
        curr.refs -= 1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root, rows, cols = TrieNode(), len(board), len(board[0])
        result, visit = set(), set()

        for w in words: root.addWord(w)

        def dfs(r: int, c: int, node: TrieNode, word: string):
            if (r not in range(0, rows) or
                c not in range(0, cols) or
                (r, c) in visit or
                board[r][c] not in node.children or
                node.children[board[r][c]].refs < 1
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                node.word = False
                result.add(word)
                root.removeWord(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)

# @lc code=end

