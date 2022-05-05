class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        goal = "123450"
        d = {0: [1, 3], 1: [0, 2, 4], 2:[1, 5], 3:[0, 4], 4:[1, 3, 5], 5:[2, 4]}
        
        state = "".join(str(c) for c in board[0] + board[1])
        
        visited = set()
        
        start = state.index('0')
        
        queue = deque([(start, state, 0)])
        
        while queue:
            cur, state, step = queue.popleft()
            if state == goal:
                return step
            elif state in visited:
                continue
            else:
                visited.add(state)
                for nxt in d[cur]:
                    tmp = list(state)
                    tmp[cur], tmp[nxt] = tmp[nxt], tmp[cur]
                    tmp = ''.join(tmp)
                    queue.append((nxt, tmp, step + 1))
        
        return -1
                
        
        