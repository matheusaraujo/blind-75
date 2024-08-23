#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root: TreeNode, lower, upper):
            if not root: return True
            if root.val <= lower or root.val >= upper: return False
            if not isValid(root.left, lower, root.val): return False
            if not isValid(root.right, root.val, upper): return False
            return True

        return isValid(root, -math.inf, math.inf)

# @lc code=end

