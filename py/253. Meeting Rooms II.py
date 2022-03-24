import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        hq = []

        for i in intervals:
            if hq and hq[0] <= i[0]:
                heapq.heapreplace(hq, i[-1])
            else:
                heapq.heappush(hq, i[-1])

        return len(hq)
