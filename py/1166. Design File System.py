class TrieNode:
    def __init__(self, value=0):
        self.next = dict()
        self.value = value


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == '/':
            return False

        folders = path.split('/')[1:]
        node = self.root

        for i, f in enumerate(folders):
            if f not in node.next:
                if i != len(folders) - 1:
                    return False
                node.next[f] = TrieNode(value)
                return True
            node = node.next[f]

        return False

    def get(self, path: str) -> int:
        folders = path.split('/')[1:]
        node = self.root

        for i, f in enumerate(folders):
            if f not in node.next:
                return -1
            node = node.next[f]

        return node.value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
