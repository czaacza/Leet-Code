class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isdigit():
                stack.append(int(tokens[i]))
            else:
                first = stack.pop()
                second = stack.pop()
                element = None

                if tokens[i] == '+':
                    element = second + first
                elif tokens[i] == '-':
                    element = second - first
                elif tokens[i] == '*':
                    element = second * first 
                elif tokens[i] == '/':
                    element = int(second / first)

                stack.append(element)

        return stack.pop()

                

        