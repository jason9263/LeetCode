"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        if not root:
            return 0
        ans = float('-inf')

        def helper(node):
            nonlocal ans
            if not node:
                return 0

            anstmp = []
            for i in node.children:
                anstmp.append(helper(i))
            anstmp.sort()

            if len(anstmp) >= 2:
                ans = max(ans, anstmp[-1] + anstmp[-2] + 1)
            elif len(anstmp) == 1:
                ans = max(ans, anstmp[-1] + 1)
            else:
                ans = max(ans, 1)

            return anstmp[-1] + 1 if len(anstmp) > 0 else 1

        helper(root)

        return ans - 1
