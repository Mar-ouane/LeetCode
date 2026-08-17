class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""

        start, end = 0, 0  # indices of best palindrome found so far

        def expand_around_center(left: int, right: int) -> int:
            # expand while characters match, return length of palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # loop stops one step too far, so real length is:
            return right - left - 1

        for i in range(len(s)):
            len1 = expand_around_center(i, i)       # odd-length palindrome centered at i
            len2 = expand_around_center(i, i + 1)    # even-length palindrome centered between i, i+1
            max_len = max(len1, len2)

            if max_len > (end - start + 1):
                # recover start/end indices from center i and max_len
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]