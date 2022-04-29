# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0

        def dfs(node, target):
            nonlocal ans
            if not node:
                return
            test(node, target)
            dfs(node.left, target)
            dfs(node.right, target)

        def test(node, target):
            nonlocal ans
            if not node:
                return

            if node.val == target:
                ans += 1

            test(node.left, target - node.val)
            test(node.right, target - node.val)

        dfs(root, targetSum)
        return ans
