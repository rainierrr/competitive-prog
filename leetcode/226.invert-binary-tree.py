#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if root is None or (root.right is None and root.left is None):
          return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

# @lc code=end

