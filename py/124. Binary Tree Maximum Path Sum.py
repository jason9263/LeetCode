# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float('-inf')

        def helper(root):
            nonlocal max_sum

            if not root:
                return 0

            l = max(helper(root.left), 0)
            r = max(helper(root.right), 0)

            pathsum = l + root.val + r
            max_sum = max(max_sum, pathsum)

            return root.val + max(l, r)

        helper(root)

        return max_sum
