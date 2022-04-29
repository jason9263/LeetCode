class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        sign = 1
        stack = []
        
        for ss in s:
            if ss.isdigit():
                num = num * 10 + int(ss)
            elif ss in ['+', '-']:
                ans = ans + sign * num
                num = 0
                sign = [-1, 1][ss == '+']
            elif ss == '(':
                stack.append(ans)
                stack.append(sign)
                sign = 1
                ans = 0
            elif ss == ')':
                ans = ans + sign * num
                ans = ans * stack.pop()
                ans = ans + stack.pop()
                num = 0
                
        return ans + sign * num
                
        