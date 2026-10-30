class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:  
        true_count = [0] * 26
        for c in s1:
            true_count[ord(c) - ord('a')] += 1

        running_count = [0] * 26
        l, f = 0, 0

        while f < len(s2):

            index = ord(s2[f]) - ord('a')

            # Shrink window until we can add s2[f]
            while running_count[index] >= true_count[index] and l < f:
                running_count[ord(s2[l]) - ord('a')] -= 1
                l += 1

            # If this character isn't allowed, skip it
            if true_count[index] == 0:
                l = f + 1
                f += 1
                continue

            running_count[index] += 1
            f += 1

            # Every character in window is valid
            if f - l == len(s1):
                return True

        return False