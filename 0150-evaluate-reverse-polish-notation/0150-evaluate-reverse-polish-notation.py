class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens: 
            if x not in "+-/*":
                stack.append(int(x))
                #print(stack)
            else:
                b = stack.pop()
                a = stack.pop()
                if x == "*":
                    ans = a*b
                elif x == "/":
                    ans = int(a/b)
                elif x == "+":
                    ans = a+b
                elif x == "-":
                    ans = a-b
                stack.append(ans)
        return stack.pop()
