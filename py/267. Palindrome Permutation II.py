class Solution:
    def generatePalindromes(self, s: str) -> List[str]:

        if not s:
            return None

        s = list(s)
        ans = set()
        halfsize = len(s) // 2
        counter = Counter(s)

        if sum(v % 2 for v in counter.values()) >= 2:
            return None

        def divid():
            nonlocal counter
            mid = ''
            for i in counter:
                if counter[i] % 2 == 0:
                    counter[i] = counter[i] // 2
                else:
                    counter[i] = (counter[i] - 1) // 2
                    mid = i
            return mid

        def permutation(tmp, counter, mid):
            if len(tmp) == halfsize:
                l = "".join(tmp)
                ans.add(l + mid + l[::-1])
                return

            for i in counter:
                if counter[i] > 0:
                    counter[i] -= 1
                    permutation(tmp + [i], counter, mid)
                    counter[i] += 1

        mid = divid()
        permutation([], counter, mid)

        return list(ans)
