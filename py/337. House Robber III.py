# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root):
        def with_without_rob(root):

            if root:
                with_l, without_l = with_without_rob(root.left)
                with_r, without_r = with_without_rob(root.right)
                return (root.val + without_l + without_r, max(with_l, without_l) + max(with_r, without_r))
            return (0, 0)

        return max(with_without_rob(root))
