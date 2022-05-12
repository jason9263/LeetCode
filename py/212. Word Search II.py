class Trie:
    def __init__(self):
        self.root = {}
    
    def addWord(self, word):
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]            
        cur['-'] = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])        
        res = []

        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        def helper(i, j, word, node):
            if '-' in node:
                res.append(word)
                del node['-']
            
            if i < 0 or j < 0 or i == m or j == n :
                return
            
            tmp = board[i][j]
            
            if tmp == '#':
                return
            if tmp not in node:
                return
            
            curnode = node[tmp]
            
            board[i][j] = '#'
                
            helper(i + 1, j, word + tmp, curnode)
            helper(i - 1, j, word + tmp, curnode)
            helper(i, j - 1, word + tmp, curnode)
            helper(i, j + 1, word + tmp, curnode)
            
            board[i][j] = tmp
            
            if not curnode:
                node.pop(tmp)

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root:   
                    helper(i, j, "", trie.root)
                
        return res
                        