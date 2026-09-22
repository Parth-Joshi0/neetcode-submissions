class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = dict()
        if len(s) != len(t):
            return False

        for cs, ct in zip(s, t):
            dict_s[cs] = dict_s.get(cs, 0)+1
            dict_s[ct] = dict_s.get(ct, 0)-1
        
        return not any(dict_s.values())