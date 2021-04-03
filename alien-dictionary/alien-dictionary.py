from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        d = defaultdict(list)
        indegree = Counter()
        q = deque()
        allChars = set(c for word in words for c in word)
        
        for i in range(len(words)-1):
            curr_word = words[i]
            next_word = words[i+1]
            
            if len(curr_word) > len(next_word) and next_word == curr_word[ : len(next_word)]:
                return ""
            
            for ch1, ch2 in zip(curr_word, next_word):
                if ch1 != ch2:
                    d[ch1].append(ch2)
                    indegree[ch2] += 1 
                    break
        
        for k in allChars:
            if indegree[k] == 0:
                q.append(k)
        
        res = [] 
        
        while q:
            curr = q.popleft()
            res.append(curr)
            
            for ch in d[curr]:
                indegree[ch] -= 1 
                
                if indegree[ch] == 0 and ch in allChars:
                    q.append(ch)
    
        output = ''.join(res)
        return output if len(output) == len(allChars) else ""
                    