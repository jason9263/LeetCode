class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if not expression:
            return []
        
        mem = {}
        def helper(s):
            if s.isdigit():
                mem[s] = [int(s)]
                return [int(s)]
            
            if s in mem:
                return mem[s]
            
            tmp_ans = []
            for i in range(len(s)):
                if s[i] in ['+', '-', '*']:
                    l = helper(s[:i])
                    r = helper(s[i+1:])
                    
                    for l_num in l:
                        for r_num in r:
                            if s[i] == '+':
                                tmp_ans.append(l_num + r_num)
                            elif s[i] == '-':
                                tmp_ans.append(l_num - r_num)
                            elif s[i] == '*':
                                tmp_ans.append(l_num * r_num)
            mem[s] = tmp_ans
                
            return tmp_ans
        
        return helper(expression)
                            