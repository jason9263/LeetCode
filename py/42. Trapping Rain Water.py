class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        lmax = height[0]
        rmax = height[-1]
        
        while l <= r:
            if height[l] <= height[r]:
                lmax = max(lmax, height[l])
                ans += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                ans += rmax - height[r]
                r -= 1
        
        return ans
                
        