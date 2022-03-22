class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s

        l, r = 0, 0
        start = 0
        ans = 0

        def helper(l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        for i in range(len(s)):
            l, r = i, i
            cur = max(helper(l, r), helper(l, r + 1))
            if cur > ans:
                ans = cur
                start = i - (cur - 1) // 2

        return s[start: (ans + start)]
