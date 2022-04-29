from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isFile = False
        self.content = ""
        self.name = ""


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        res = []
        path = path.split('/')[1:]
        cur = self.root
        if path[0] != '':
            for p in path:
                cur = cur.child[p]
        if cur.isFile:
            return [cur.name]
        for ch in cur.child:
            res.append(ch)
        return sorted(res)

    def populatePath(self, path):
        cur = self.root
        paths = path.split('/')[1:]
        for p in paths:
            cur = cur.child[p]
            cur.name = p
        return cur

    def mkdir(self, path: str) -> None:
        self.populatePath(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.populatePath(filePath)
        cur.isFile = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.populatePath(filePath)
        if cur.isFile:
            return cur.content
