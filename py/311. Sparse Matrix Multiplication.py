class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = []
        if not mat1 or not mat2:
            return ans
        m = len(mat1)
        n = len(mat1[0])
        k = len(mat2)
        l = len(mat2[0])
        
        if n != k:
            return ans
        
        ans = [[0] * l for i in range(m)]
        
        dic_y = {}
        for k, row in enumerate(mat2):
            dic_y[k] = {}
            for l, v in enumerate(row):
                dic_y[k][l] = v
        
        for m, row in enumerate(mat1):
            for k, v1 in enumerate(row):
                if v1:
                    for l, v2 in dic_y[k].items():
                        ans[m][l] += v1*v2
        
        return ans
            
        