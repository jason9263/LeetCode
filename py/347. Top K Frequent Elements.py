class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        
        counter = Counter(nums)
        fre = [[] for _ in range(len(nums) + 1)]
        
        for key, v in counter.items():
            fre[v].append(key)
        
        ans = []
        for i in range(len(nums), 0, -1):
            for n in fre[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        
        