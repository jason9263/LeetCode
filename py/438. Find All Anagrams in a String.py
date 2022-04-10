class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []

        lp = [0] * 26
        ls = [0] * 26
        lenp = len(p)
        
        for c in p:
            lp[ord(c) - ord('a')] += 1

        ans = []
        
        for i in range(0, len(s)):
            c = s[i]    
            if i >= lenp:
                ls[ord(s[i - lenp]) - ord('a')] -= 1
            ls[ord(c) - ord('a')] += 1
            
            if lp == ls:
                ans.append(i - lenp + 1)
                
        return ans
            
            