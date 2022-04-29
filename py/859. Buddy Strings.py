class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal and len(set(s)) < len(s):
            return True
        
        diff = []
        for i, j in zip(s, goal):
            if i != j:
                diff.append((i, j))
                
        if len(diff) == 2 and diff[0] == diff[1][::-1]:
            return True
        
        return False
        