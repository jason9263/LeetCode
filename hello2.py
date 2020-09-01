class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or not k:
            return 0

        cnt = 0
        dic = dict()

        sum_x = 0
        dic[0] = 1

        for i in range(len(nums)):
            sum_x += nums[i]
            cnt += dic.get(sum_x - k, 0)
            dic[sum_x] = dic.get(sum_x, 0) + 1

        return cnt
