import collections
import heapq


def find_shortest_paths_3(node_q, src, dest, weight):
    g = collections.defaultdict(list)
    for s, d, w in zip(src, dest, weight):
        g[s].append(d)
        g[d].append(s)
        g[(s, d)] = w
        g[(d, s)] = w

    dist = collections.defaultdict(lambda: float('inf'))
    dist[1] = 0
    q = [(0, 1)]
    # parent = collections.
    relaxed = set()
    parent = collections.defaultdict(set)

    def relaxation(g, u, v):
        if dist[v] > dist[u]+g[(u, v)]:
            dist[v] = dist[u]+g[(u, v)]
            parent[v] = set()
        if dist[v] == dist[u]+g[(u, v)]:
            parent[v].add(u)

    def dfs(parent, node, min_edges):
        print(node)
        parents = parent[node]
        for p in parents:
            min_edges.append((node, p))
            dfs(parent, p, min_edges)

    while(q):
        _, u = heapq.heappop(q)
        for nei in g[u]:
            if nei not in relaxed:
                relaxation(g, u, nei)
                heapq.heappush(q, (dist[nei], nei))
        relaxed.add(u)
    min_edges = []
    ans = []
    dfs(parent, node_q, min_edges)
    for s, d in zip(src, dest):
        if (s, d) in min_edges or (d, s) in min_edges:
            ans.append('YES')
        else:
            ans.append('NO')
    return ans


if __name__ == '__main__':
    ans = find_shortest_paths_3(
        5,
        [1, 2, 3, 4, 5, 1, 5],
        [2, 3, 4, 5, 1, 3, 3],
        [1, 1, 1, 1, 3, 2, 1]
    )
    print(ans)
