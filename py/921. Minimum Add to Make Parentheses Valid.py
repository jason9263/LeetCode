class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        if not s:
            return 0

        for i in range(len(s)):
            c = s[i]
            if not stack:
                stack.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)

        return len(stack)
