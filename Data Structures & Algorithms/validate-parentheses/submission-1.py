class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {
            '(':')',
            '{':'}',
            '[':']'
        }

        stack = []

        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                if not stack or open_close_map[stack[-1]] != char:
                    return False
                stack.pop()
        
        return not stack