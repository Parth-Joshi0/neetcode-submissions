class Solution:
    def isValid(self, s: str) -> bool:
        c = {')': '(', '}': '{', ']': '['}
        stack = ['x']
        for bracket in s:
            if bracket in c:
                if stack.pop() != c[bracket]:
                    return False
            else:
                stack.append(bracket)
        
        return len(stack) == 1
