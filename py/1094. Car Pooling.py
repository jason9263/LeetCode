import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hq = []
        trips.sort(key = lambda x : x[1])
        
        for c, s, e in trips:
            while hq and hq[0][0] <= s:
                capacity += hq[0][1]
                heapq.heappop(hq)
            
            if c > capacity:
                return False
            else:
                capacity -= c
                heapq.heappush(hq, (e, c))
        
        return True
                