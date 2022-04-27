class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if not routes or source == target:
            return 0

        g = defaultdict(set)

        for busnumber, stops in enumerate(routes):
            for stop in stops:
                g[stop].add(busnumber)

        seen_bus = set()
        seen_stop = set()

        q = deque()
        ans = 0
        q.append((source, ans))

        while q:
            size = len(q)
            for i in range(size):

                trans, ans = q.popleft()
                if trans == target:
                    return ans

                for bus in g[trans]:
                    if bus not in seen_bus:
                        seen_bus.add(bus)
                        for stop in routes[bus]:
                            if stop not in seen_stop:
                                q.append((stop, ans + 1))
                                seen_stop.add(stop)

        return -1
