class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_chars(word):
            l = [0] * 26
            for char in word:
                l[ord(char) - ord('a')] += 1
            return str(l)

        d = dict()
        for word in strs:
            x = count_chars(word)
            if x not in d:
                d[x] = [word]
            else:
                d[x].append(word)

        return list(d.values())