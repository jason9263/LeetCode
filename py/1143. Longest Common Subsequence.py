class Solution:
    
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        M, N = len(a), len(b)
        t = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for m in range(1, M+1):
            for n in range(1, N+1):
                if a[m-1] == b[n-1]:
                    t[m][n] = 1 + t[m-1][n-1]
                else:
                    t[m][n] = max(t[m][n-1], t[m-1][n])
        
        return t[M][N]
    