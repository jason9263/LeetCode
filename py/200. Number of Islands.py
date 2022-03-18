class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ans = 0
        m = len(grid)
        n = len(grid[0])     
        
        def helper(grid, i, j, m, n):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                
            if i + 1 <= m - 1 and grid[i + 1][j] == '1':
                helper(grid, i + 1, j, m, n)
            
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                helper(grid, i - 1, j, m, n)
            
            if j + 1 <= n - 1 and grid[i][j + 1] == '1':
                helper(grid, i, j + 1, m, n)
            
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                helper(grid, i, j - 1, m, n)
             
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    helper(grid, i, j, m, n)
                    ans += 1
                    
        return ans
                    
        