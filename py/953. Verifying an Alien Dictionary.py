class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words or not order:
            return False
        dic = defaultdict(int)
        index = 0
        for c in order:
            dic[c] = index
            index += 1

        def helper(w1, w2):
            nonlocal dic
            m = len(w1)
            n = len(w2)
            for i in range(min(m, n)):
                if dic[w1[i]] < dic[w2[i]]:
                    return True
                elif dic[w1[i]] == dic[w2[i]]:
                    continue
                else:
                    return False

            if m > n:
                return False

            return True

        for i in range(1, len(words)):
            if not helper(words[i-1], words[i]):
                return False

        return True
