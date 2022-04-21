from collections import deque

a = [[1, 2], [4], [6], [], [7, 8, 9]]
ans = [1, 4, 6, 7, 2, 8, 9]


def solution(a):
    ind = [0] * len(a)
    skip = [False] * len(a)
    while not all(skip):
        for i in range(len(a)):
            if ind[i] < len(a[i]):
                print(a[i][ind[i]])
                ind[i] += 1
            else:
                skip[i] = True


class iteratorInferface:
    def __init__(self, a) -> None:
        self.ind = [0] * len(a)
        self.jump = [False] * len(a)
        self.cur_a = 0
        self.num = []
        self.cur_num = 0
        while not all(self.jump):
            for i in range(len(a)):
                if self.ind[i] < len(a[i]):
                    print(a[i][self.ind[i]])
                    self.num.append(a[i][self.ind[i]])
                    self.ind[i] += 1
                else:
                    self.skip[i] = True

    def hasNext(self):
        return not all(self.jump)

    def next(self):

    def reset(self):
        self.ind = [0] * len(a)
        self.jump = [False] * len(a)
        self.cur = 0


itera = iteratorInferface(a)

print(itera.hasNext())
print(itera.next())
