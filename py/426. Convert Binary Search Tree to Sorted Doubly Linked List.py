"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        pre = None
        dummy = Node(-1, None, None)
        pre = dummy
        def helper(node):
            nonlocal pre
            
            if not node:
                return

            helper(node.left)

            pre.right = node
            node.left = pre
            pre = node

            helper(node.right)
        
        helper(root)
        pre.right = dummy.right
        dummy.right.left = pre
        
        return dummy.right
                
        