class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = set()

        g = {w: i for i, w, in enumerate(words)}

        for index, w in enumerate(words):
            rev = w[::-1]
            size = len(w)
            for i in range(size + 1):

                if w[:i] == rev[size - i:]:
                    if rev[:size - i] in g:
                        ans.add((g[rev[:size - i]], index))

                if w[i:] == rev[:size - i]:
                    if rev[size - i:] in g:
                        ans.add((index, g[rev[size - i:]]))

        return [x for x in ans if x[0] != x[1]]
