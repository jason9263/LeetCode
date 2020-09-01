# Given an array of integer and a target value. Find the subsequence that sum to the target number.
# [1,2,3,3], 6 -> [0, 2] (1+2+3=6) or [2,3] -> (3 + 3 = 6).
#  0 1 2 3

# if there is a subsequence, return the start and end index (zero based).
# [1,2,1,2,4], 5 -> 2+1+2 =5, return [1, 3]

# helper presum array[00 0-1  0-j ]

# presum(j)- presum(i) == target
# I return the i j
# O(N^2)


from collections import defaultdict


def find_index(num, target):
    # defensive coding
    if not num or len(num) == 0:
        return [-1, -1]

    # pre sum. array
    presum = [0] * (len(num) + 1)
    presumHash = defaultdict(int)
    presumHash[0] = 0

    for i in range(len(num)):
        presum[i + 1] = presum[i] + num[i]
    print(presum)

    for i in range(1, len(presum)):
        tmp_target = presum[i] - target
        if tmp_target in presumHash.keys():
            print(tmp_target, presum[i])
            l = presumHash[tmp_target]
            return [l, i-1]
        # build hashmap here.
        presumHash[presum[i]] = i

    return [-1, -1]


num = [1, 2, 3, 3]
target = 6

num = [1, 2, 1, 2, 4]
target = 5
res = find_index(num, target)

print(res)
