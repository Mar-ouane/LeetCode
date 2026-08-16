class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 128  # ASCII range
        left = 0
        maxi = 0

        for right in range(len(s)):
            c = ord(s[right])
            if last_seen[c] >= left:
                left = last_seen[c] + 1
            last_seen[c] = right
            length = right - left + 1
            if length > maxi:
                maxi = length

        return maxi
