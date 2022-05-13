# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def dfs(node):
            f = [0] * (distance + 1)
            if not node:
                return f, 0

            if not node.left and not node.right:
                f[0] = 1
                return f, 0

            fl, pl = dfs(node.left)
            fr, pr = dfs(node.right)

            pairs = 0
            for dl, cl in enumerate(fl):
                for dr, cr in enumerate(fr):
                    pairs += (cl * cr) if dl + dr + 2 <= distance else 0

            for i in range(distance):
                f[i+1] = fl[i] + fr[i]

            return f, pl + pr + pairs

        return dfs(root)[1]
