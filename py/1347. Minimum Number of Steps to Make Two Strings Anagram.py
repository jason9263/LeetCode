class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(t) - Counter(s)).values())
        