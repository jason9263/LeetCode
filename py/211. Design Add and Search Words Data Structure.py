class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node['$'] = True

    def search(self, word: str) -> bool:

        def dfs(word, node):
            for i, w in enumerate(word):
                if w not in node:
                    if w == '.':
                        for x in node:
                            if x != '$' and dfs(word[i+1:], node[x]):
                                return True
                    return False
                else:
                    node = node[w]
            return '$' in node

        return dfs(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
