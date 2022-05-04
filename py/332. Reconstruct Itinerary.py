class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []

        tickets.sort()

        g = defaultdict(list)

        for t in tickets:
            g[t[0]].append(t[1])

        def helper(src, tmp):
            nonlocal g, ans, tickets
            if len(tmp) == len(tickets) + 1:
                ans = list(tmp)
                return True

            if src not in g:
                return False

            for i, v in enumerate(g[src]):
                tmp.append(v)
                g[src].remove(v)
                if helper(v, tmp):
                    return True
                tmp.pop()
                g[src].insert(i, v)

            return False

        helper('JFK', ['JFK'])

        return ans
