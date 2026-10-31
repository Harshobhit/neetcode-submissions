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
                stack_top = stack[-1]
                if open_close_map[stack_top] != char:
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False