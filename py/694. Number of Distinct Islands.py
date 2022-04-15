class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        ans = set()

        m = len(grid)
        n = len(grid[0])
        dirc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        tmpans = []
        
        def helper(x, y, i, j, tmpans):
            nonlocal grid
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 0
                tmpans.append((x - i, y - j))
                for dx, dy in dirc:
                    helper(x + dx, y + dy, i, j, tmpans)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tmpans = []
                    helper(i, j, i, j, tmpans)
                    ans.add(str(tmpans))
        
        return len(ans)
            
        