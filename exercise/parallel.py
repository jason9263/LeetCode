class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        if not N:
            return 0

        visited, graph, indegrees = set(), collections.defaultdict(list), \
            [0] * (N + 1)
        for relation_x, relation_y in relations:
            graph[relation_x].append(relation_y)
            indegrees[relation_y] += 1

        topological_stack = collections.deque()
        for index, indegree in enumerate(indegrees[1:], start=1):
            if not indegree:
                topological_stack.append((index, 1))

        semesters = 1
        while topological_stack:
            curr_course, semester = topological_stack.popleft()
            semesters = max(semesters, semester)
            visited.add(curr_course)
            for course in graph[curr_course]:
                indegrees[course] -= 1
                if not indegrees[course]:
                    topological_stack.append((course, semester + 1))

        if len(visited) == N:
            return semesters
        return -1
