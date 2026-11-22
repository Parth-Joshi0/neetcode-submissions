class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters = {'2' : ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'), '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}

        res = []
        if digits == "":
            return res
        def backtrack(index, curr):
            if index == len(digits):
                res.append(curr)
                return
            for c in num_to_letters[digits[index]]:
                backtrack(index+1, curr + c)
        
        backtrack(0, '')
        return res