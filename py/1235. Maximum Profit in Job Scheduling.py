class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        dp = [[0, 0]]

        for s, e, p in jobs:
            idx = bisect.bisect_right(dp, [s + 1]) - 1
            if dp[idx][1] + p > dp[- 1][1]:
                dp.append([e, dp[idx][1] + p])

        return dp[-1][1]


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort(key=lambda x: x[1])  # sort by end time

        def find_right(dp, s):
            # find the last item that <= s
            l, r = 0, len(dp)-1
            while l <= r:
                mid = (l+r)//2
                e = dp[mid][0]
                if e <= s:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
        # endtime, total profit
        dp = [(0, 0)]
        for s, e, p in jobs:
            last = find_right(dp, s)
            if dp[last][1] + p > dp[-1][1]:
                dp.append((e, dp[last][1] + p))

        return dp[-1][1]
