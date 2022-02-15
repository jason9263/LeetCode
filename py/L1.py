class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        if not differences:
            return 0
        
        
        def subn(diff, base, size, bench, lower, upper):
            for i in range(bench-1, -1):
                base[i] = base[i+1] - diff[i]
                if base[i] > upper or base[i] < lower:
                    return False
            return True
        
        def addn(diff, base, size, bench, lower, upper):
            for i in range(bench + 1, size):
                base[i] = base[i-1] + diff[i]
                if base[i] > upper or base[i] < lower:
                    return False
            return True
        
        diff = [0] + differences
        size = len(diff)
        base = [0] * size
        cnt = 0
        for i in range(1, size):
            for x in range(lower, upper+1):
                base[i] = x
                if subn(diff, base, size, i, lower, upper) and addn(diff, base, size, i, lower, upper):
                    cnt += 1

        return cnt
                