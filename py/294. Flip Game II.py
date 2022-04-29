class Solution:
    def canWin(self, currentState: str) -> bool:
        seen = {}

        def helper(s):
            nonlocal seen
            if not s or len(s) < 2:
                return False

            if s in seen:
                return seen[s]

            for i in range(len(s) - 1):
                if s[i] == '+' and s[i+1] == '+' and not helper(s[:i] + '--' + s[i+2:]):
                    seen[s] = True
                    return True

            seen[s] = False
            return False

        return helper(currentState)
