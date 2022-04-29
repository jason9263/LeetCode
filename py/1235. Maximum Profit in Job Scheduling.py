class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        dp = [[0, 0]]

        for s, e, p in jobs:
            idx = bisect.bisect_right(dp, [s + 1]) - 1
            if dp[idx][1] + p > dp[- 1][1]:
                dp.append([e, dp[idx][1] + p])

        return dp[-1][1]
