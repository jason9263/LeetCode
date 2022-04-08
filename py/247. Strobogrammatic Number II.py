class Solution:
    def findStrobogrammatic(self, n: int):
        ans = []
        if n <= 0:
            return ans
        dic = defaultdict(str)

        dic["0"] = "0"
        dic["1"] = "1"
        dic["8"] = "8"
        dic["6"] = "9"
        dic["9"] = "6"

        def dfs(tmp, ans):
            if len(tmp) == n:
                if len(tmp) == 1 or (len(tmp) > 1 and tmp[0] != '0'):
                    # print(tmp)
                    ans.append(tmp)
                return

            for k, v in dic.items():
                dfs(k + tmp + v, ans)

        if (n % 2 == 1):
            dfs("0", ans)
            dfs("1", ans)
            dfs("8", ans)
        else:
            dfs("", ans)

        return ans
