class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if not nums:
            return []

        size = len(nums)

        def dfs(comb, counter):
            if len(comb) == size:
                ans.append(comb)
                return

            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    dfs(comb + [num], counter)
                    counter[num] += 1

        dfs([], Counter(nums))

        return ans
