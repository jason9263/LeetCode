class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        r_b = 0
        c_b = 0
        r_e = len(matrix)-1 
        c_e = len(matrix[0])-1
        while (r_b <= r_e and c_b <= c_e):
            for i in range(c_b,c_e+1):
                res.append(matrix[r_b][i])
            r_b += 1
            for i in range(r_b,r_e+1):
                res.append(matrix[i][c_e])
            c_e -= 1
            if (r_b <= r_e):
                for i in range(c_e,c_b-1,-1):
                    res.append(matrix[r_e][i])
                r_e -= 1
            if (c_b <= c_e):
                for i in range(r_e,r_b-1,-1):
                    res.append(matrix[i][c_b])
                c_b += 1
        return res
    