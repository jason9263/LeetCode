
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        def helper(nl):
            tmp = []
            for n in nl:
                if n.isInteger():
                    tmp.append(n)
                else:
                    tmp.extend(helper(n.getList()))

            return tmp

        self.n = helper(nestedList)
        self.it = 0
        self.capacity = len(self.n)

    def next(self) -> int:
        if self.it < self.capacity:
            ans = self.n[self.it]
            self.it += 1
            return ans

    def hasNext(self) -> bool:
        return self.it < self.capacity
