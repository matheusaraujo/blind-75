#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global ans
        ans = root.val

        def dfs(root: Optional[TreeNode]) -> int:
            if not root: return 0

            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))

            global ans
            ans = max(ans, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)

        dfs(root)

        return ans

# @lc code=end

