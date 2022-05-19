class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        if not strs:
            return 0
        
        g = defaultdict(list)
        
        for s in strs:
            g[s] = [s]
            
        def similar(a, b):
            cnt = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    cnt += 1
                if cnt > 2:
                    return False
            
            return cnt == 2
        
        def buildG(g):
            size = len(strs)
            for i in range(size):
                a = strs[i]
                for j in range(i + 1, size):
                    b = strs[j]
                    if similar(a, b):
                        g[a].append(b)
                        g[b].append(a)
        
        def dfs(a):
            nonlocal g, visited
            for i in g[a]:
                if i in visited:
                    continue
                else:
                    visited.add(i)
                    dfs(i)
                    
        cnt = 0
        visited = set()
        buildG(g)
        for i in range(len(strs)):
            a = strs[i]
            if a not in visited:
                cnt += 1
                visited.add(a)
                dfs(a)

        return cnt
                    