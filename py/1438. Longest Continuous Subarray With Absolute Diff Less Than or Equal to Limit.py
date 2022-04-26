class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums or limit < 0:
            return 0

        maxdq = deque()
        mindq = deque()

        ans = 0
        l = 0

        for r in range(len(nums)):

            while maxdq and nums[maxdq[-1]] <= nums[r]:
                maxdq.pop()

            maxdq.append(r)

            while mindq and nums[mindq[-1]] >= nums[r]:
                mindq.pop()

            mindq.append(r)

            while maxdq and mindq and nums[maxdq[0]] - nums[mindq[0]] > limit:
                l += 1

                if l > maxdq[0]:
                    maxdq.popleft()

                if l > mindq[0]:
                    mindq.popleft()

            ans = max(ans, r - l + 1)

        return ans
