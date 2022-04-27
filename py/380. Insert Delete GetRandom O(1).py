from random import choice


class RandomizedSet:

    def __init__(self):
        self.dic = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False

        index = len(self.arr)
        self.dic[val] = index
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False

        tmpindex = self.dic[val]
        self.dic[self.arr[-1]] = tmpindex
        self.arr[tmpindex] = self.arr[-1]

        del self.dic[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
