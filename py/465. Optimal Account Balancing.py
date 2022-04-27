class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        if not transactions:
            return 0

        debt = defaultdict(int)
        for f, t, a in transactions:
            debt[f] -= a
            debt[t] += a

        dlist = [val for key, val in debt.items() if val != 0]

        def helper(k, dl):
            if k == len(dl):
                return 0

            if dl[k] == 0:
                return helper(k + 1, dlist)

            cur = dl[k]
            min_trans = float('inf')

            for i in range(k + 1, len(dl)):
                d_next = dl[i]
                if (cur * d_next < 0):
                    dl[i] = cur + d_next
                    min_trans = min(min_trans, 1 + helper(k + 1, dl))
                    dl[i] = d_next

                    if cur + d_next == 0:
                        break
            return min_trans

        return helper(0, dlist)
