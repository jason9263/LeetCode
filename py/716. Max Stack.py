class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack:
            m = max(x, self.stack[-1][1])
            self.stack.append((x, m))
        else:
            self.stack.append((x, x))

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()[0]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def peekMax(self) -> int:
        if self.stack:
            return self.stack[-1][1]

    def popMax(self) -> int:
        m = self.stack[-1][1]
        b = []

        while self.stack[-1][0] != m:
            b.append(self.stack.pop())

        self.stack.pop()

        while b:
            self.push(b.pop()[0])

        return m
