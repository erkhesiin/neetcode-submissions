class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        length = len(s)
        l = 0
        _map = {}

        for r in range(length):
            if s[r] in _map:
                l = max(_map[s[r]] + 1, l)
            _map[s[r]] = r
            result = max(result, r - l + 1)

        return result