class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        sc = Counter(s)
        ans = 0

        for key, v in sc.items():
            if v % 2:
                ans += 1

        return ans <= k
