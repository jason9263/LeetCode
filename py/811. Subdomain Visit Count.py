import re


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return None

        ans = []
        dic = defaultdict(int)

        for dp in cpdomains:
            dplist = re.split(r'[.|\s]', dp)
            tmp = []
            for i in range(len(dplist)-1, 0, -1):
                tmp = [dplist[i]] + tmp
                dic[".".join(tmp)] += int(dplist[0])

        for k, v in dic.items():
            s = str(v) + " " + str(k)
            ans.append(s)

        return ans
