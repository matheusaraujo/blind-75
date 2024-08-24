#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def find(self, word: str) -> Optional[TrieNode]:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return None
            curr = curr.children[c]
        return curr

    def search(self, word: str) -> bool:
        f = self.find(word)
        return f and f.end

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

