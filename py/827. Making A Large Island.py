class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        color_ = 2
        dic = defaultdict(int)
        dic[0] = 0

        def getarea(x, y):
            nonlocal grid, color_, m, n
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1:
                return 0
            grid[x][y] = color_
            return 1 + getarea(x - 1, y) + getarea(x + 1, y) + getarea(x, y - 1) + getarea(x, y + 1)

        def getcolor(x, y):
            nonlocal grid, m, n
            return 0 if (x < 0 or y < 0 or x >= m or y >= n) else grid[x][y]

        ans = float('-inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tmp = getarea(i, j)
                    dic[color_] = tmp
                    ans = max(ans, tmp)
                    color_ += 1

#         print(color_, grid, dic)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    colorset = set(
                        [getcolor(i - 1, j), getcolor(i + 1, j), getcolor(i, j - 1), getcolor(i, j + 1)])
                    tmp = 1
                    for c in colorset:
                        tmp += dic[c]
                    ans = max(ans, tmp)

        return ans
