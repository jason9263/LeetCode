class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict or not s:
            return False

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for r in range(1, len(s) + 1):
            for l in range(0, r):
                if dp[l] and s[l:r] in wordDict:
                    dp[r] = True
                    break

        return dp[-1]
