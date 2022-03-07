# 设计内存文件系统模拟实现如下功能：

# ls：给定路径字符串，若对应一个目录，则输出其中包含的目录和文件（字典序）；若对应一个文件，则只输出该文件名

# mkdir：创建目录，若目录不存在，则递归创建缺少的目录

# addContentToFile：在文件中追加内容，若文件不存在，则新建

# readContentFromFile：从文件中读取内容并返回

# 注意：

# 你可以假设文件和目录的路径均为绝对路径，以/开始，并且结尾不包含/，除非路径就是"/"本身
# 你可以假设所有操作均合法，用户不会常识读取一个不存在的文件，或者ls一个不存在的目录
# 你可以假设所有目录名称和文件名称都只包含小写字母，并且在同一目录下不会存在同名的目录或者文件


# Time:  ls: O(l + klogk), l is the path length, k is the number of entries in the last level directory
#        mkdir: O(l)
#        addContentToFile: O(l + c), c is the content size
#        readContentFromFile: O(l + c)
# Space: O(n + s), n is the number of dir/file nodes, s is the total content size.

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

    def mkdir(self, path: str) -> None:
        cur = self.root
        paths = path.split('/')[1:]
        for p in paths:
            cur = cur.child[p]
            cur.name = p

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        filePath = filePath.split('/')[1:]
        for p in filePath:
            cur = cur.child[p]
            cur.name = p
        cur.isFile = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        filePath = filePath.split('/')[1:]
        for p in filePath:
            cur = cur.child[p]
        if cur.isFile:
            return cur.content
------------------------------------------------------------------
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
