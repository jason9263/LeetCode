# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(target, node, tmp):
            nonlocal ans
            if not node:
                return

            if not node.left and not node.right and node.val == target:
                tmp += [node.val]
                ans.append(list(tmp))
                return

            if node.left:
                dfs(target - node.val, node.left, tmp + [node.val])

            if node.right:
                dfs(target - node.val, node.right, tmp + [node.val])

        dfs(targetSum, root, [])

        return ans
