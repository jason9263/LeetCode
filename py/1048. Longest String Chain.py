class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        d = {word: 1 for word in words}

        ans = 1

        for word in words:
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in d:
                    d[word] = max(1 + d[prev], d[word])
                    ans = max(ans, d[word])

        return ans
