class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = []
        
        for o in order:
            ans.append(o * count[o])
            count[o] = 0
            
        for c in count:
            ans.append(c * count[c])
        
        return "".join(ans)
        