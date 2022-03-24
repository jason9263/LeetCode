class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        def helper(s1, s2):
            if len(s1) == 0 or len(s2) == 0:
                return ""
            length = min(len(s1), len(s2))
            i = 0
            while i < length:
                if s1[i] != s2[i]:
                    break
                else:
                    i += 1
            if i < length:
                return s1[0:i]
            else:
                return s1[0:length]

        s1 = min(strs)
        s2 = max(strs)

        return helper(s1, s2)


        