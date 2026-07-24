class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            print(i)
            print(stack)
            match i:
                case "+":
                    x = int(stack.pop())
                    stack.append(int(stack.pop())+x)
                case "-":
                    x = int(stack.pop())
                    stack.append(int(stack.pop())-x)
                case "*":
                    x = int(stack.pop())
                    stack.append(int(stack.pop())*x)
                case "/":
                    x = int(stack.pop())
                    stack.append(int(stack.pop())/x)
                case _:
                    stack.append(i)
        return int(stack.pop())