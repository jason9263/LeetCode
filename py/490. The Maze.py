class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not maze[0]:
            return False

        m = len(maze)
        n = len(maze[0])
        stack = []
        stack.append((start[0], start[1]))

        visited = set()
        visited.add((start[0], start[1]))

        dirc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while stack:
            x, y = stack.pop()
            if [x, y] == destination:
                return True
            for dx, dy in dirc:
                new_x = x
                new_y = y
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and not (maze[new_x + dx][new_y + dy]):
                    new_x += dx
                    new_y += dy
                if (new_x, new_y) not in visited:
                    stack.append((new_x, new_y))
                    visited.add((new_x, new_y))

        return False
