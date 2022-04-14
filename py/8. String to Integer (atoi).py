class Solution:
    def myAtoi(self, s: str) -> int:        
        s=s.lstrip()           #strip is used to delete extra spaces .(lstrip is used to delete spaces which are on left )

        if len(s)==0:
            return 0        
        result=0       
        sign = 1
        start=0
        if s[0]=='-':                
            sign=-1
            start=1              #starting position becomes one after this step
        if s[0]=='+':
            start=1       
        while start<len(s):
            if not ('0'<=s[start]<='9'):            # If anything other than 0 to 9 comes it'll break and give the results (it is comparing the ascii value of strings)

                if result*sign>=2**31-1:
                    return 2**31-1
                if result*sign <= -2147483648:
                    return -2147483648
                else:
                    return result*sign            

            result=result*10 + (ord(s[start])-ord('0'))          # ord() function gives ascii value of any character , in this step we are generating the number . { ord(start)-ord('0') } this gives us the single digit . 
            #ord('0') will give value 48 so by subtracting it from any other digit ascii value will give us the digit . 

            start+=1

        if result*sign>=2**31-1:
                return 2**31-1
        if result*sign <= -2147483648:
                return -2147483648

        return sign*result
        