class Solution:
    def findOrder(self, numCourses, prerequisites):
        sortedorder = []
        if numCourses <= 0:
            return False
        inDegree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        for child, parent in prerequisites:
            graph[parent].append(child)
            inDegree[child] += 1

        sources = deque()

        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()

            sortedorder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        if len(sortedorder) != numCourses:
            return []
        return sortedorder
