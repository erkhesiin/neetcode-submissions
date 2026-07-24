class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = ''
        for c in s:
            if c.isalnum():
                cs += c.lower()
        return cs == cs[::-1]