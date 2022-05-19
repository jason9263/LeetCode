class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        dq = deque()
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    dq.append((i, j, 0))
                    break

        while dq:
            x, y, d = dq.popleft()
            for mx, my in moves:
                nx = x + mx
                ny = y + my
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] in ['#', 'O']:
                    if grid[nx][ny] == '#':
                        return d + 1
                    grid[nx][ny] = '|'
                    dq.append((nx, ny, d + 1))

        return -1
