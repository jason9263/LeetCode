# import itertools


# a = itertools.permutations([-1, 1, -2, 2], 2)
# for i in a:
#     print(i)

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0

        ans, x, y = 0, abs(x), abs(y)
        dq = deque()
        dq.append((0,0))
        seen = set()
        
        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, -1), (-2, 1)]
        while dq:
            quelen = len(dq)
            ans += 1
            for i in range(quelen):  
                cur_x, cur_y = dq.popleft()
                for move in moves:
                    new_x = cur_x + move[0]
                    new_y = cur_y + move[-1]
                    if -2 <= new_x <= x + 2 and -2 <= new_y <= y + 2 and (new_x, new_y) not in seen:
                        if new_x == x and new_y == y:
                            return ans
                        dq.append((new_x, new_y))
                        seen.add((new_x, new_y))

        return ans
        