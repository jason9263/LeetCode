# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        colTable = defaultdict(list)
        min_col = max_col = 0

        def dfs(node, row, col):
            if node is not None:
                nonlocal min_col, max_col
                colTable[col].append((row, node.val))
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        res = []

        for col in range(min_col, max_col + 1):
            res.append([val for row, val in sorted(colTable[col])])

        return res
