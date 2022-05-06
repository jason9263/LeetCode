def solution(a, t):
    a.sort()
    ans = set()
    
    def dfs(tmp, t):
        if len(tmp) == len(t):
            ans.add(tmp)
            
    