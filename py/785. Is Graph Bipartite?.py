class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return False
        
        size = len(graph)
        visited = [0] * size
        
        dq = deque()
        
        def helper(i):
            nonlocal dq, visited
            dq.append((i, graph[i]))
            visited[i]  = 1

            while dq:
                index, children = dq.popleft()
                for c in children:
                    if visited[c] == 0:
                        visited[c] = (2 if visited[index] == 1 else 1)
                        dq.append((c, graph[c]))
                    elif visited[c] == visited[index]:
                        return False
            return True

        
        for i in range(size):
            if visited[i] == 0 and not helper(i):
                return False

        return True
            
        
        