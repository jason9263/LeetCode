class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        if not words:
            return []
        
        wcounter = Counter(words)
        
        ans = sorted(wcounter, key = lambda x: (-wcounter[x], x))
        
        return ans[:k]
        