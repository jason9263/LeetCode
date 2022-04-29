class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = []
        i = 0

        for px, py in points:
            if px == x or py == y:
                heapq.heappush(ans, (abs(px - x) + abs(py - y), i))
            i += 1

        return heapq.heappop(ans)[1] if len(ans) else -1
