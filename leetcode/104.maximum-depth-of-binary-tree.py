from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      if root is None:
        return 0

      q = deque([[root,1]])

      while(True):
        node_info  = q.popleft()

        node = node_info[0]
        depth = node_info[1]

        for child_node in [node.left, node.right]:
          if child_node is None:
            continue

          q.append([child_node, depth+1])
        if len(q) == 0:
          return depth
