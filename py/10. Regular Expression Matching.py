class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return False
        n = len(p)
        m = len(s)
        dp = [[False] * (n+1) for _ in range(m+1)]
        
        dp[0][0] = True
        for i in range(1 ,n + 1):
            if i >= 2 and p[i-1] == "*" and dp[0][i-2]:
                dp[0][i] = True
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1] == '*':
                        if p[j-2] != s[i-1] and p[j-2] != '.':
                            dp[i][j] = dp[i][j-2]
                        else:
                            dp[i][j] = (dp[i][j-2] or dp[i][j-1] or dp[i-1][j])
        
        return dp[m][n]
        