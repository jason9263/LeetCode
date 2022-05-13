class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([])

        q.append((0, 0, 0, k))

        seen = set()

        while q:
            r, c, steps, rk = q.popleft()

            if r == m - 1 and c == n - 1:
                return steps
            else:
                for x, y in moves:
                    nx = x + r
                    ny = y + c
                    if nx >= 0 and nx < m and ny >= 0 and ny < n and (nx, ny, rk) not in seen:
                        if grid[nx][ny] == 1 and rk > 0:
                            seen.add((nx, ny, rk))
                            q.append((nx, ny, steps + 1, rk - 1))
                        elif grid[nx][ny] == 0:
                            seen.add((nx, ny, rk))
                            q.append((nx, ny, steps + 1, rk))

        return -1
