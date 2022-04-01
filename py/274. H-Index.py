class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        citations.sort()
        
        size = len(citations)
        hindex = float('-inf')
        
        for i in range(size):
            hindex = max(min(citations[i], size - i), hindex)

        return hindex
                
        