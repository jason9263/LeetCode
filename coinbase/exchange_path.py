from collections import defaultdict
from email.policy import default


g = {
    "A": {"B": 6, "D": 1},
    "B": {"A": 6, "D": 2, "E": 2, "C": 5},
    "D": {"A": 1, "B": 2, "E": 1},
    "E": {"B": 2, "D": 1, "C": 5},
    "C": {"B": 5, "E": 5}
}


def pathprod(s, t, g):

    def helper(cur, path, seen):
        if cur == t:
            return 1, path

        ans_path = []
        ans_prod = 0

        if cur in g:
            for neighbor in g[cur]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    prod_, path_ = helper(neighbor, path + [neighbor], seen)
                    if ans_prod < prod_ * g[cur][neighbor]:
                        ans_prod = prod_ * g[cur][neighbor]
                        ans_path = path_
                    seen.remove(neighbor)

        return ans_prod, ans_path

    return helper(s, [s], {s})


s = "A"
t = "C"
print(pathprod(s, t, g), type(g))


g = {"BTC-USD": {"ask": "12", "bid": "14"},
     "ETH-USD": {"ask": "23", "bid": "31"}}


def graph(g):
    gra = defaultdict(defaultdict)
    for k, v in g.items():
        s, t = k.split('-')
        gra[s][t] = 1 / int(v['ask'])
        print(s, t, v, gra[s][t])


graph(g)
