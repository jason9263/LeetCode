class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        front, back = set([beginWord]), set([endWord])
        wordDict = set(wordList)

        if endWord not in wordDict:
            return 0

        length = 2

        def newWordSet(words):
            ans = set()
            for word in words:
                for i in range(len(word)):
                    for _ in range(0, 26):
                        tmp_w = word[:i] + chr(_ + ord('a')) + word[i+1:]
                        ans.add(tmp_w)
            return ans

        while front:
            front = wordDict & newWordSet(front)

            if front & back:
                return length

            length += 1

            if len(front) > len(back):
                front, back = back, front

            wordDict -= front

        return 0
