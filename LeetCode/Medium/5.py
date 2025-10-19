class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            odd = expand(i, i)
            # Even length palindrome
            even = expand(i, i + 1)

            # Update longest if found longer
            longest = max(longest, odd, even, key=len)
        return longest
