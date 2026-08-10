class Solution:
    def isValid(self, s: str) -> bool:
        match_elements = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in match_elements:
                if stack and stack[-1] == match_elements[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return True if not stack else False

