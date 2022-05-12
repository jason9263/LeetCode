class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordList = set(wordList)
        n = len(beginWord)

        found, swapped = False, False
        start_q, end_q = {beginWord}, {endWord}
        paths, res = collections.defaultdict(set), []

        while start_q and not found:
            next_q = set()
            wordList -= set(start_q)
            for word in start_q:
                for i in range(n):
                    first, second = word[:i], word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = first+c+second
                        if new_word in wordList:
                            if new_word in end_q:
                                found = True
                            else:
                                next_q.add(new_word)

                            paths[new_word].add(
                                word) if swapped else paths[word].add(new_word)

            start_q = next_q

            if len(start_q) > len(end_q):
                start_q, end_q = end_q, start_q
                swapped = not swapped

        res = []

        def bfs(word, cur_path):
            if word == endWord:
                cur_path.append(word)
                res.append(cur_path[::])
                return
            else:
                for parent in paths[word]:
                    bfs(parent, cur_path+[word])
        bfs(beginWord, [])
        return res
