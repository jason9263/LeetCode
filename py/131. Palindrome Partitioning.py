class Solution:
    def partition(self, s: str) -> List[List[str]]:

        if not s or len(s) == 0:
            return ans
        
        def ispalin(st):
            return st == st[::-1]
        
        ans = []
        tmpans = []
        def helper(l):
            nonlocal ans, tmpans, s
            if l >= len(s):
                ans.append(tmpans.copy())
                return
            for j in range(l, len(s)):
                if ispalin(s[l:j + 1]):
                    tmpans.append(s[l:j + 1])
                    helper(j + 1)
                    tmpans.pop()
        
        helper(0)
        return ans
    
        