class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        while l < r:

            m = (l + r) // 2
            k = 0
            for q in quantities:
                k += q // m + (q % m != 0)

            if k > n:
                l = m + 1
            else:
                r = m

        return l
