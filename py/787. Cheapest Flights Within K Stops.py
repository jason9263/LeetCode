class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [float('inf') for _ in range(n)]
        dp[src] = 0

        for source, des, tp in flights:
            if source == src:
                dp[des] = tp

        for transfer in range(0, K):
            c_dp = [*dp]
            for s, d, tp in flights:
                c_dp[d] = min(c_dp[d], dp[s] + tp)

            dp = c_dp

        if dp[dst] == float('inf'):
            return -1
        else:
            return dp[dst]
