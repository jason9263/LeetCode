import time


def dfs_num(depth, m, n, sm, sn, memo):
    if depth == 0:
        if n != 0 and abs(m / n - 7/5) <= 0.001:
            return 1
            #print(sm, sn, res)
        return 0

    if (depth, m, n) in memo:
        return memo[(depth, m, n)]

    res = 0

    for i in (2, 5, 7):
        res += dfs_num(depth - 1, m + i, n, sm + str(i), sn + "0", memo)
        res += dfs_num(depth - 1, m, n + i, sm + "0", sn + str(i), memo)

    memo[(depth, m, n)] = res

    return res


test_round = 8

start_time = time.time()

res = dfs_num(test_round, 0, 0, "", "", {})
print(res)
print("--- %s seconds ---" % (time.time() - start_time))


def dfs_path(depth, m, n, sm, sn, res):
    if depth == 0:
        if n != 0 and abs(m / n - 7/5) <= 0.001:
            res += 1
            #print(sm, sn, res)
        return res

    for i in (2, 5, 7):
        res = dfs_path(depth - 1, m + i, n, sm + str(i), sn + "0", res)
        res = dfs_path(depth - 1, m, n + i, sm + "0", sn + str(i), res)
    return res


start_time = time.time()
res = dfs_path(test_round, 0, 0, "", "", 0)
print(res)
print("--- %s seconds ---" % (time.time() - start_time))


def dfs_num_simple(depth, m, n,  memo):
    if depth == 0:
        if n != 0 and abs(m / n - 7/5) <= 0.001:
            return 1
            #print(sm, sn, res)
        return 0

    if (depth, m, n) in memo:
        return memo[(depth, m, n)]

    res = 0

    for i in (2, 5, 7):
        res += dfs_num_simple(depth - 1, m + i, n, memo)
        res += dfs_num_simple(depth - 1, m, n + i, memo)

    memo[(depth, m, n)] = res

    return res


test_round = 8

start_time = time.time()

res = dfs_num_simple(test_round, 0, 0, {})
print(res)
print("--- %s seconds ---" % (time.time() - start_time))


def dfs_path_simple(depth, m, n,  res):
    if depth == 0:
        if n != 0 and abs(m / n - 7/5) <= 0.001:
            res += 1
            #print(sm, sn, res)
        return res

    for i in (2, 5, 7):
        res = dfs_path_simple(depth - 1, m + i, n, res)
        res = dfs_path_simple(depth - 1, m, n + i,  res)
    return res


start_time = time.time()
res = dfs_path_simple(test_round, 0, 0, 0)
print(res)
print("--- %s seconds ---" % (time.time() - start_time))
