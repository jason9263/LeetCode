class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(rooms)
        n = len(rooms[0])
        inf = 2147483647
        q = deque()
        
        def helper(x, y, dis):
            nonlocal rooms
            if x >= 0 and x < m and y >= 0 and y < n and rooms[x][y] == inf:
                q.append((x, y, dis))
                rooms[x][y] = dis
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        
        while q:
            x, y, dis = q.popleft()
            for move in moves:
                nx = x + move[0]
                ny = y + move[1]
                helper(nx, ny, dis + 1)
        
        
        return rooms
            