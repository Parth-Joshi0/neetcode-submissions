class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for c in tokens:
            if c == "+":
                nums.append(nums.pop() + nums.pop())
            elif c == "-":
                x = nums.pop()
                y = nums.pop()
                nums.append(y - x)
            elif c == "*":
                nums.append(nums.pop() * nums.pop())
            elif c == "/":
                x = nums.pop()
                y = nums.pop()
                nums.append(int(y / x))
            else:
                nums.append(int(c))
        return nums.pop()
        