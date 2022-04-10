class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        heapq.heapify(self.heap)
        self.capacity = k

        if not nums:
            return

        for i in range(len(nums)):
            if i < self.capacity:
                heapq.heappush(self.heap, nums[i])
            else:
                heapq.heappushpop(self.heap, nums[i])

    def add(self, val: int) -> int:
        if len(self.heap) == self.capacity:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)

        return self.heap[0]
