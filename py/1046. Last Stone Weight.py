class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]

        exp = [-x for x in stones]
        heapq.heapify(exp)

        while len(exp) > 1:
            max_1 = abs(heapq.heappop(exp))
            max_2 = abs(heapq.heappop(exp))

            diff = max_1 - max_2
            if diff > 0:
                heapq.heappush(exp, -diff)

        return -heapq.heappop(exp) if len(exp) == 1 else 0
