class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def backtrack(start):
            if start == len(s):
                res.append(partition.copy())
                return
            
            for i in range(start, len(s)):
                if s[start:i+1] == s[start:i+1][::-1]:
                    partition.append(s[start:i+1])
                    backtrack(i+1)
                    partition.pop()
        
        backtrack(0)
        return res