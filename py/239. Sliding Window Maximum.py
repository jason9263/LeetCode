class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        if not nums or k <= 0 or k > len(nums):
            return ans

        l = 0
        q = deque()

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if q and r >= k - 1:
                ans.append(nums[q[0]])
                l += 1

        return ans
