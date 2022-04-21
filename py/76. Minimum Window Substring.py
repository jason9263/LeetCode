class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        c_t = Counter(t)
        formed = len(c_t)

        count = 0
        l, r = 0, 0
        ans = (float('inf'), None, None)
        d_s = defaultdict(int)

        while r < len(s):
            c = s[r]
            d_s[c] += 1

            if c in c_t and d_s[c] == c_t[c]:
                count += 1

                while l <= r and count == formed:
                    c = s[l]

                    if r - l + 1 < ans[0]:
                        ans = (r - l + 1, l, r)

                    d_s[c] -= 1

                    if c in c_t and d_s[c] < c_t[c]:
                        count -= 1

                    l += 1

            r += 1

        return "" if ans[0] == float('inf') else s[ans[1], ans[2] + 1]
