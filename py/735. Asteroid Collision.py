class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if abs(ans[-1]) < abs(new):
                    ans.pop()
                    continue
                elif abs(ans[-1]) == abs(new):
                    ans.pop()
                break
            else:
                ans.append(new)

        return ans
