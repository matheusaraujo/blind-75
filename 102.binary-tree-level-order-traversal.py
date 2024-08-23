#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # ans = []

        # def dfs(node: TreeNode, depth: int):
        #     if not node: return
        #     if len(ans) <= depth: ans.append([])
        #     ans[depth].append(node.val)
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)

        # dfs(root, 0)

        # return ans

        ans, q = [], deque()

        if root: q.append(root)

        while q:
            v = []

            for i in range(len(q)):
                node = q.popleft()
                v.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            ans.append(v)

        return ans


# @lc code=end

