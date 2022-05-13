class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(x, y):
            nonlocal m, n, board
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                board[x][y] = '.'
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

        for row in [0, m - 1]:
            for col in range(n):
                if board[row][col] == 'O':
                    dfs(row, col)

        for col in [0, n - 1]:
            for row in range(1, m - 1):
                if board[row][col] == 'O':
                    dfs(row, col)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'
