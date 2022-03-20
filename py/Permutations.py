class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        ans = []
        tmp = []
        size = len(nums)
        visited = set()

        def dfs(res, tmp):
            if len(tmp) == size:
                res.append(tmp)
                return
            for i in range(size):
                if i not in visited:
                    visited.add(i)
                    dfs(res, tmp + [nums[i]])
                    visited.remove(i)

        dfs(ans, tmp)

        return ans
