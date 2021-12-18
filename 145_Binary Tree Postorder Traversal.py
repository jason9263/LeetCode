# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = collections.deque()
        stack = []
        p = root

        while stack or p:
            if p:
                stack.append(p)
                res.appendleft(p.val)
                p = p.right
            else:
                p = stack.pop()
                p = p.left

        return res
