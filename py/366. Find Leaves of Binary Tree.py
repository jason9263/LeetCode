# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        ans = []
        def dfs(node):
            nonlocal dic
            if not node:
                return -1
            l = dfs(node.left)
            r = dfs(node.right)
            val = max(l, r) + 1
            dic[val].append(node.val)
            return val
        
        dfs(root)
        
        for i in range(len(dic)):
            ans.append(dic[i])
            
        return ans
        
            