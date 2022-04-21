import random


class connectfour:
    def __init__(self) -> None:
        self.row = 6
        self.col = 7
        self.threshold = 4
        self.dir = [[1, 0], [0, 1],
                    [1, 1], [1, -1]]
        self.board = [[0 for _ in range(self.col)] for _ in range(self.row)]
        self.row_index = [0 for _ in range(self.col)]

    def printboard(self, board):
        m = len(board)
        print("Board :")
        for i in range(m - 1, -1, -1):
            print(board[i])

    def simpleai(self, col):
        return random.randint(0, col)

    def connect_four(self):
        row = self.row
        col = self.col

        curr = 0
        while True:
            player = 1 if curr % 2 == 0 else 2
            # y = int(input(f'player {player} column choice? '))
            y = self.simpleai(col - 1)
            x = self.row_index[y]
            if x < 0 or x >= row or y < 0 or y >= col or self.board[x][y] != 0:
                print('bad move!')
                continue
            self.board[x][y] = player
            self.row_index[y] += 1

            if self.check_winning(self.board, x, y, row, col, player):
                print(f'player {player} has won the game!')
                return

            curr += 1
            if curr == row * col:
                print(f'game tie!')
                return

    def check_winning(self, board, x, y, row, col, current_player):

        self.printboard(board)
        print(x, y, current_player)
        for i in range(len(self.dir)):
            ans = 1
            for sign in [1, -1]:
                for step in range(1, self.threshold):
                    newx = sign * step * self.dir[i][0] + x
                    newy = sign * step * self.dir[i][1] + y
                    if newx >= 0 and newx < row and newy >= 0 and newy < col:
                        if board[newx][newy] == current_player:
                            ans += 1
                            if ans == 4:
                                return True
                        else:
                            break

        return False


c4 = connectfour()
c4.connect_four()
