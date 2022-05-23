class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                r = stack.pop()
                l = stack.pop()
                if i == "+":
                    stack.append(r + l)
                elif i == "-":
                    stack.append(l - r)
                elif i == "*":
                    stack.append(r * l)
                elif i == "/":
                    stack.append(int(float(l) / r))

        return stack[-1]
