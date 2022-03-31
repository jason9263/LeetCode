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
        
        def compressM(mat):
            r = len(mat)
            c = len(mat[0])
            ans = [[] for _ in range(r)]
            
            for r, row in enumerate(mat):
                for c, v in enumerate(row):
                    if v:
                        ans[r].append((v, c))
            return ans
                    
        
        ans = [[0] * l for i in range(m)]
        
        A = compressM(mat1)
        B = compressM(mat2)
        
        for i in range(m):
            for v1, c1 in A[i]:
                for v2, c2 in B[c1]:
                    ans[i][c2] += v1*v2
        
        return ans
            
        