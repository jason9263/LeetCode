class Node:
    def __init__(self, key, value, active) -> None:
        self.key = key
        self.value = value
        self.active = active
        self.children = []


class Menu:
    def __init__(self):
        pass

    def same(self, a, b):
        if not a and not b:
            return True

        if (not a and b) or (a and not b):
            return False

        return a.key == b.key and a.value == b.value and a.active == b.active

    def getChildrenMap(self, a):
        dic = {}
        if not a:
            return dic

        for c in a.children:
            dic[c.key] = c

        return dic

    def getModified(self, a, b):
        if not a and not b:
            return 0

        cnt = 0

        if not a or not b or not self.same(a, b):
            cnt += 1

        childaMap = self.getChildrenMap(a)
        childbMap = self.getChildrenMap(b)

        for k in childaMap.keys():
            cnt += self.getModified(childaMap[k],
                                    childbMap[k] if k in childbMap else None)

        for k in childbMap.keys():
            if k not in childaMap:
                cnt += self.getModified(None, childbMap[k])

        return cnt


a = Node("a", 1, True)
b = Node("b", 2, True)
c = Node("c", 3, True)
d = Node("d", 4, True)
e = Node("e", 5, True)
f = Node("f", 6, True)
g = Node("g", 7, True)

a.children.append(b)
a.children.append(c)

b.children.append(d)
b.children.append(e)

c.children.append(g)

a1 = Node("a", 1, True)
b1 = Node("b", 2, True)
c1 = Node("c", 3, True)
d1 = Node("d", 4, True)
e1 = Node("e", 5, True)
f1 = Node("f", 6, True)
g1 = Node("g", 7, False)

a1.children.append(b1)
a1.children.append(c1)

b1.children.append(d1)
b1.children.append(e1)
b1.children.append(f1)

c1.children.append(g1)

m = Menu()
count = m.getModified(a, a1)

print(count)
