class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.dp[0][0] = matrix[0][0]

        for i in range(1, m):
            self.dp[i][0] = matrix[i][0] + self.dp[i-1][0]

        for i in range(1, n):
            self.dp[0][i] = matrix[0][i] + self.dp[0][i-1]

        for i in range(1, m):
            for j in range(1, n):
                self.dp[i][j] = self.dp[i][j-1] + self.dp[i-1][j] - \
                    self.dp[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        if row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1-1]
        if col1 == 0:
            return self.dp[row2][col2] - self.dp[row1-1][col2]
        if row2 >= row1 and col2 >= col1:
            return self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
