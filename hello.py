def generateParenthesis(n):
    def dfs(s, left, right):
        if len(s) == 2*n:
            res.append(s)
            return

        if left < n:
            dfs(s + '(', left + 1, right)

        if right < left:
            dfs(s + ')', left, right + 1)

    res = []
    dfs('', 0, 0)
    return res



generateParenthesis(3)