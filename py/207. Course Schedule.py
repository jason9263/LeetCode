class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for i in range(numCourses):
            graph[i] = []
            indegree[i] = 0
            
        for course in prerequisites:
            graph[course[1]].append(course[0])
            indegree[course[0]] += 1
        
        dq = deque()
        
        for k, v in indegree.items():
            if v == 0:
                dq.append(k)
        

        ans = []
        while dq:
            cur = dq.popleft()
            ans.append(cur)
            for i in graph[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    dq.append(i)
        
        return len(ans) == numCourses
            
        
        
            