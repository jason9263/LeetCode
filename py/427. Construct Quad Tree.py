"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid or not grid[0]:
            return None
        m = len(grid)
        n = len(grid[0])
        
        def helper(sx, sy, ex, ey):
            nonlocal grid

            val = grid[sx][sy]
            same = True
            
            for i in range(sx, ex + 1):
                for j in range(sy, ey + 1):
                    if grid[i][j] != val:
                        same = False
                        break
                if not same:
                    break
            
            if same:
                node = Node(1 if val else 0, True, None, None, None, None)
                return node
            else:
                midx = (sx + ex) // 2
                midy = (sy + ey) // 2
                ul = helper(sx, sy, midx, midy)
                ur = helper(sx, midy + 1, midx, ey)
                bl = helper(midx + 1,  sy, ex, midy)
                br = helper(midx + 1, midy + 1, ex, ey)
                node = Node(val, False, ul, ur, bl, br)
                return node
            
        return helper(0, 0, m - 1, n - 1)

        