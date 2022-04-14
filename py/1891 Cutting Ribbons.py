class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l = 0
        r = sum(ribbons) // k + 1
        
        def helper(mid):
            nonlocal k, ribbons
            res = 0
            for i in ribbons:
                res += i // mid
                if res >= k:
                    return True
            return False
        
        while(l < r):
            mid = r - ((r - l) >> 1)
            if helper(mid):
                l = mid
            else:
                r = mid -1
        return l
    