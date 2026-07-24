from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = deque()
        mapping = {')': '(', '}': '{', ']': '['}
        for c in s:
            if (c == '(' or
                c == '{' or
                c == '['
                ):
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != mapping[c]:
                    return False

        return len(stack) == 0