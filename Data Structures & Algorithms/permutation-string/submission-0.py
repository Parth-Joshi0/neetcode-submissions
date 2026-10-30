class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        true_count = [0] * 26
        running_count = [0] * 26

        for c in s1:
            true_count[ord(c) - ord('a')] += 1

        l = 0

        for f in range(len(s2)):
            # Add the rightmost character
            running_count[ord(s2[f]) - ord('a')] += 1

            # Remove leftmost character if window is too large
            if f - l + 1 > len(s1):
                running_count[ord(s2[l]) - ord('a')] -= 1
                l += 1

            # Check if the window matches
            if running_count == true_count:
                return True

        return False