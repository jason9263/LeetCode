class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1
        
        while l <= r:
            mid = l + ((r - l) >> 1)            
            tmp = matrix[mid // n][ mid % n]

            if tmp == target:
                return True
            if tmp < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
            