class Solution:
    def knightDialer(self, n: int) -> int:
        h = {}
        h[0] = [4, 6]
        h[1] = [6, 8]
        h[2] = [7, 9]
        h[3] = [4, 8]
        h[4] = [0, 3, 9]
        h[5] = []
        h[6] = [0, 1, 7]
        h[7] = [2, 6]
        h[8] = [1, 3]
        h[9] = [2, 4]
        
        dp = [[0] * 10 for _ in range(n + 1)]
        modnumber = 10 ** 9 + 7
        
        for i in range(1, n + 1):
            for j in range(10):
                if i == 1:
                    dp[i][j] = 1
                else:
                    for k in h[j]:
                        dp[i][j] += dp[i-1][k]
                    
                    dp[i][j] = dp[i][j] % (modnumber)
                        
        ans = 0
        for i in range(10):
            ans += dp[n][i]
            
        return ans % (modnumber)
