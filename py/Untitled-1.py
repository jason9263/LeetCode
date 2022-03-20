from collections import Counter


a = [1, 1, 1, 2, 3, 4, 54, 5]
c = Counter(a)

if 2 in c:
    c[2] = c[2] - 1
    del c[2]
    print('hello world')

print(c.items())
