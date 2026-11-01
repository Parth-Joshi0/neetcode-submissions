class Solution:
    def minWindow(self, s: str, t: str) -> str:
        frequency = [0] * 52
        # Get the frequency map of t, since order does not matter
        for char in t:
            frequency[self.get_index(char)] += 1
        
        left_border, right_border = 0, 0
        window_frequency = [0] * 52
        res = ""
        # frequency of the window to check if substring has the valid  chars
        while right_border != len(s):
            window_frequency[self.get_index(s[right_border])] += 1
            right_border += 1
            if self.equals(window_frequency, frequency):
                while self.equals(window_frequency, frequency):
                    window_frequency[self.get_index(s[left_border])] -= 1
                    left_border += 1
                if res == "" or len(s[left_border-1:right_border]) < len(res):
                    res = s[left_border-1:right_border]
        return res
    
    def equals(self, window_frequency, frequency):
        for i, j in zip(window_frequency, frequency):
            if j > i:
                return False
        return True

    def get_index(self, char):
        if 'a' <= char <= 'z':
            return ord(char) - ord('a')
        else:
            return ord(char) - ord('A') + 26