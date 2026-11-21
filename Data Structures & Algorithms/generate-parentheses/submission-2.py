class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, left, right):
            if left == 0 and left == right:
                res.append(curr)
                return
            if right > left:
                backtrack(curr + ')', left, right-1)
            if left > 0:
                backtrack(curr + '(', left - 1, right)

        backtrack("", n, n)
        return res
            