class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ans = []
        for i in range(len(currentState)-1):
            if currentState[i] == currentState[i+1] and currentState[i] == '+':
                tmp = currentState[:i] + '--' + currentState[i + 2:]
                ans.append(tmp)
        
        return ans
                
        