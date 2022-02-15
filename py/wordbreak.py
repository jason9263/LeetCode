# Author: Huahua
class Solution:
  def calculate(self, s: str) -> int:
    nums = []
    op = '+'
    cur = 0
    i = 0
    while i < len(s):
      if s[i] == ' ': 
        i += 1
        continue
      while i < len(s) and s[i].isdigit():
        cur = cur * 10 + ord(s[i]) - ord('0')
        i += 1      
      if op in '+-':
        nums.append(cur * (1 if op == '+' else -1))
      elif op == '*':
        nums[-1] *= cur
      elif op == '/':
        sign = -1 if nums[-1] < 0 or cur < 0 else 1
        nums[-1] = abs(nums[-1]) // abs(cur) * sign
      cur = 0
      if (i < len(s)): op = s[i]
      i += 1    
    return sum(nums)