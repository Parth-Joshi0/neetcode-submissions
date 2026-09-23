class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))
            encoded += "彍"
            encoded += word
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        num = ""
        while i < len(s):
            if s[i] == '彍':
                num = int(num)
                word = ""
                for x in range(num):
                    word += s[x+i+1]
                decoded.append(word)
                i += num
                num = ""
            else:
                num += s[i]
            i += 1
                    
        return decoded
