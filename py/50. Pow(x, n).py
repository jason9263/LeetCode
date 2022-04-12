class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 0

        dic = defaultdict(int)
        dic[0] = 1
        dic[1] = x
        ans = 0

        def helper(x, n):
            nonlocal dic, ans
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n in dic:
                return dic[n]

            if n % 2 == 1:
                ans = x * helper(x, n // 2) * helper(x, n // 2)
            else:
                ans = helper(x, n // 2) * helper(x, n // 2)

            dic[n] = ans
            return ans

        helper(x, abs(n))
        return dic[abs(n)] if n >= 0 else (1 / dic[abs(n)])
