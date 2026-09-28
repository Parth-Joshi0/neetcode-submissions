class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = "".join(char for char in s if char.isalnum())
        return x == x[::-1]
