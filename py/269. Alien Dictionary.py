class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""
        
        graph = {}
        indegree = {}
        
        for word in words:
            for c in word:
                graph[c] = []
                indegree[c] = 0
        
        #build graph
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            
            index = 0;
            length = min(len(w1), len(w2))
            flag = len(w1) > len(w2)
            
            while index < length and w1[index] == w2[index]:
                index += 1
                
            if index == length and flag:
                return ""
            if index < length:
                graph[w1[index]].append(w2[index])
                indegree[w2[index]] += 1
        
        seed = [];
        
        for k, v in indegree.items():
            if v == 0:
                seed.append(k)
        ans = []
        
        while seed:
            cur = seed.pop(0)
            ans.append(cur)
            for i in graph[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    seed.append(i)
        
        return ''.join(ans) if len(ans) == len(indegree) else ""
            