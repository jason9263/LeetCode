from typing import BinaryIO


def say_hello():
    print('Hello, World')


for i in range(5):
    say_hello()

"""
HTML Formatting
===============

Input text - for example, "ABCDE"
Input formats - a map of HTML tags, to the ranges over which that HTML tag should apply in the text, where a range is a start and an end index. for example {"b": [[0, 2]]}

Output: The string with the HTML tags inserted in the right place, so we could render insert.

1. text = "ABCDE"
   formats = {"b": [[0, 2]]}

   output = "<b>AB</b>CDE"

2. text = "ABCDE"
   formats = {"b": [[0, 2]], "i": [[1, 3]], "x": [[1, 2]]}
    
   output = "<b>A<i>B</i></b><i>C</i>DE"


   <b>A<i><x>B</x></i></b><i>C</i>DE
"""

# sort the inter.start

# A -> class .val = a, opent = [] .append<x>   closet = []

# the latest end Index
# [0, 2]

# <B>   ----> 2.closet.append(\b)
# array = [0, 2]
# [0   1  --->  <-1>2<1>    <-1>3]

# sorted[  0  1 <x> ----><-x>  2  3]
# [1, 2]----->  <-x>3 <x> ---> its end index
# how to add the tag   <b>A <i>B  </b>C DE

# [  0, 1  ----> <-x>3<x>   ----><-x>  5 <x> ----   8  9]   [1  7]


# character tag
class ct:
    def __init__(self, val, index) -> None:
        self.val = val
        self.index = index
        self.opent = []
        self.closet = []

# pre processing method

# formats = {"b": [[0, 2]], "i": [[1, 3]], "x": [[1, 2]]}


def solution(text, ftags):
    ans = []
    if not text or not ftags:
        return None

    for i, c in enumerate(text):
        ans.append(ct(c, i))

    alist = [[0, 2, "b"], [1, 3, "i"], [1, 2, "x"]]

    alist.sort(key=lambda x: x[0])
    orderindex = []

    for interval in alist:
        s, e, t = interval[0], interval[1], interval[2]
        # bi-search
        if len(orderindex) == 0:
            ans[s].append(t)
            ans[e].append("/" + t)  # < >
        else:  # [0 2]  [1 3]
            i = 0
            for i in range(len(orderindex)):
                if orderindex[i] < s:
                    continue
                elif orderindex[i] >= s and orderindex[i] <= e:
                    orderindex[i].closet.append("/" + t)
                    orderidnex[i+1].openset.append(t)
