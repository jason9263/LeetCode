class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push(root)

    def next(self) -> int:
        if self.stack:
            cur = self.stack.pop()
            if cur.right:
                self.push(cur.right)

            return cur.val

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False

    def push(self, root):
        while root:
            self.stack.append(root)
            root = root.left
