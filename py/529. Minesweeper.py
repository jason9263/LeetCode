class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click[0], click[1]
        m, n = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        def helper(x, y):
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return board
            
            elif board[x][y] == 'E':
                cnt = 0
                neighbor = []
                for move in dirs:
                    new_x = x + move[0]
                    new_y = y + move[1]
                    if 0 <= new_x < m and 0 <= new_y < n:
                        neighbor.append((new_x, new_y))
                        if board[new_x][new_y] == 'M':
                            cnt += 1
                
                if not cnt:
                    board[x][y] = 'B'
                    for r, c in neighbor:
                        helper(r, c)
                else:
                    board[x][y] = str(cnt)

        helper(x, y)
        return board
                