class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        if len(cs) == 0 or len(cs) == 1:
            return True
        if cs[0] == cs[-1]:
            return self.isPalindrome(cs[1:-1])
        return False
         