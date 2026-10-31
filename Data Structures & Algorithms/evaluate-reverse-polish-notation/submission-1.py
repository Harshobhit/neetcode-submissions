class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        result = 0
        ops = ('+', '-', '*', '/')
        for token in tokens:
            if token in ops:
                b, a = int(op_stack.pop()), int(op_stack.pop())
                if token == '+':
                    op_stack.append(a+b)
                elif token == '-':
                    op_stack.append(a-b)
                elif token == '*':
                    op_stack.append(a*b)
                else:
                    op_stack.append(int(a/b))
            else:
                op_stack.append(token)
        return int(op_stack[0])