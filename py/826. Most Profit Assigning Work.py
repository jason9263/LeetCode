class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dp = list(zip(difficulty, profit))
        dp.sort()

        worker.sort()
        ans = 0
        i = 0
        maxp = 0

        for w in worker:
            while i < len(dp) and w >= dp[i][0]:
                maxp = max(maxp, dp[i][1])
                i += 1
            ans += maxp

        return ans
