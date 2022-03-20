class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None

        ans = [[]]
        for i in nums:
            ans += [cur + [i] for cur in ans]
        return ans
