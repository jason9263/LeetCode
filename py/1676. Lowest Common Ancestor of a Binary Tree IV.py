# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        
        def helper(root):
            if not root or root in nodes:
                return root
            
            left = helper(root.left)
            right = helper(root.right)
            
            if left and right:
                return root
            
            return left if left else right
        
        return helper(root)
        