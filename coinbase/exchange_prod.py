def get_currency_exchange_rate(source, target, graph):

    def backtrack(current, seen):
        if current == target:
            return 1

        product = 0
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    product = max(
                        product, graph[current][neighbor] * backtrack(neighbor, seen))
                    seen.remove(neighbor)

        return product

    return backtrack(source, {source})


g = {
    "A": {"B": 6, "D": 1},
    "B": {"A": 6, "D": 2, "E": 2, "C": 5},
    "D": {"A": 1, "B": 2, "E": 1},
    "E": {"B": 2, "D": 1, "C": 5},
    "C": {"B": 5, "E": 5}
}
curr1 = "A"
curr2 = "C"
print(get_currency_exchange_rate(curr1, curr2, g))


def solution(s, t, g):

    def helper(cur, seen):

        if cur == t:
            return 1

        prod = 0
        if cur in g:
            for neighbor in g[cur]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    prod = max(prod, g[cur][neighbor]
                               * helper(neighbor, seen))
                    seen.remove(neighbor)
        return prod

    return helper(s, {s})


s = "A"
t = "C"
print(solution(s, t, g))


def solutionpath(s, t, g):
    ans = []

    def helper(cur, path, seen):
        if cur == t:
            ans.append(path)
            return

        if cur in g:
            for neighbor in g[cur]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    helper(neighbor, path + [neighbor], seen)
                    seen.remove(neighbor)
        return

    helper(s, [s], {s})
    return ans


print(solutionpath(s, t, g))
