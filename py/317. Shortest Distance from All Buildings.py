class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        m = len(grid)
        n = len(grid[0])

        dis = [[0] * n for i in range(m)]
        visited = [[0] * n for i in range(m)]
        dir_xy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cnt = sum(val for line in grid for val in line if val == 1)

        def bfs(i, j):
            hit = [[False] * n for i in range(m)]
            q = [(i, j, 0)]
            hit[i][j] = True
            tmpcnt = 1
            while q:
                pre_x, pre_y, depth = q.pop(0)
                for i in range(4):
                    x = pre_x + dir_xy[i][0]
                    y = pre_y + dir_xy[i][1]
                    if x >= 0 and x < m and y >= 0 and y < n and not hit[x][y]:
                        hit[x][y] = True
                        if grid[x][y] == 0:
                            q.append((x, y, depth + 1))
                            visited[x][y] += 1
                            dis[x][y] += depth + 1
                        elif grid[x][y] == 1:
                            tmpcnt += 1

            return tmpcnt == cnt

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not bfs(i, j):
                        return -1

        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if visited[i][j] == cnt:
                    ans = min(ans, dis[i][j])

        return ans if ans != float('inf') else -1
