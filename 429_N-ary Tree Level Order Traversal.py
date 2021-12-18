"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = collections.deque([(root, 0)])
        while q:
            tmp, l = q.popleft()
            if len(res) < l + 1:
                res.append([])

            for child in tmp.children:
                q.append((child, l + 1))

            res[l].append(tmp.val)

        return res
