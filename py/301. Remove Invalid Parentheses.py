class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return ['']
        l, r = 0, 0
        ans = set()

        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1

        def isValid(s):
            l, r = 0, 0
            for i in s:
                if i == '(':
                    l += 1
                elif i == ')':
                    if l > 0:
                        l -= 1
                    else:
                        r += 1
            return l == 0 and r == 0

        def dfs(l, r, ind, tmp):
            tmp_s = ''.join(tmp)
            # print(tmp_s, l, r)
            if l == 0 and r == 0 and isValid(tmp_s):
                ans.add(tmp_s)
                return

            for i in range(ind, len(s)):
                if s[i] != '(' and s[i] != ')':
                    continue
                if i != ind and s[i] == s[i-1]:
                    continue
                if r > 0 and s[i] == ')':
                    tmp[i] = ''
                    dfs(l, r - 1, i + 1, tmp)
                    tmp[i] = s[i]
                elif l > 0 and s[i] == '(':
                    tmp[i] = ''
                    dfs(l - 1, r, i + 1, tmp)
                    tmp[i] = s[i]
        print(l, r)
        dfs(l, r, 0, list(s))
        return list(ans)
