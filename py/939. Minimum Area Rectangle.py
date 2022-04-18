class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if not arr:
            return 0
                
        stack = []
        
        stack.append(float('inf'))
        ans = 0
        
        for i in range(len(arr)):
            cur = arr[i]
            while stack[-1] <= cur:
                bottom = stack.pop()
                if stack[-1] < cur:
                    ans += stack[-1] * bottom
                else:
                    ans += bottom * cur
            stack.append(cur)
                
        while len(stack) > 2:
            ans += stack.pop() * stack[-1]
        
        return ans

                