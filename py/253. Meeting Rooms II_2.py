import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])

        for i in range(len(intervals)):
            intervals[i][0], intervals[i][1] = intervals[i][1], intervals[i][0]

        # hq = []
        # for x in intervals:
        #     if hq and hq[0][0] <= x[1]:
        #         heapq.heappop(hq)
        #     heapq.heappush(hq, x)

        # n = len(hq)
        # print(n)   # PART1 to find complete min number of rooms complete

        # indexes to keep track of min number of room available
        n = len(intervals)
        ans = [[]]
        hq = []
        idx = list(range(n))

        for x in intervals:
            if hq and hq[0][0] <= x[1]:
                _, _, ind = heapq.heappop(hq)
                heapq.heappush(idx, ind)

            ind = heapq.heappop(idx)
            if ind >= len(ans):
                ans.append([])
            ans[ind].append([x[1], x[0]])
            heapq.heappush(hq, (x[0], x[1], ind))

        print(ans)
        return ans  # Expected result


data = [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9], [6, 10], [7, 11], [8, 12]]
a = Solution()
a.minMeetingRooms(data)
