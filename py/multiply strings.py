class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2 or num1 == "0" or num2 == "0":
            return "0"
        
        ans = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1) -1, -1, -1):
            carry = 0
            for j in range(len(num2) -1, -1, -1):
                tmp = (ord(num2[j]) - ord('0')) * (ord(num1[i]) - ord('0'))  + carry
                carry = (ans[i+j+1] + tmp) // 10
                ans[i+j+1] = (ans[i+j+1] + tmp) % 10
            
            ans[i] += carry
            
        ans = ''.join(map(str, ans))
        
        return ans.lstrip('0')

        
        