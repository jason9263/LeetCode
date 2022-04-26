class Solution:
    def nearestPalindromic(self, n: str) -> str:
        size = len(n)
        ans = set()
        ans.add(str(10 ** size + 1))
        ans.add(str(10 ** (size - 1) - 1))

        prefix = int(n[: (size + 1) // 2])

        for pre in map(str, (prefix - 1, prefix, prefix + 1)):
            ans.add(pre + [pre, pre[:-1]][size & 1][::-1])

        ans.discard(n)

        return min(ans, key=lambda x: (abs(int(x) - int(n)), int(x)))
