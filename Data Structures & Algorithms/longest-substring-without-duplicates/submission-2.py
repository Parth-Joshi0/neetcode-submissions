class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        longest_seen = 0

        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1

            seen[s[r]] = r
            longest_seen = max(longest_seen, r - l + 1)

        return longest_seen