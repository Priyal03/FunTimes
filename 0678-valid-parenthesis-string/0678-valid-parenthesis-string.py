class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack=deque()
        star=deque()

        for i,x in enumerate(s):
            if x == '(':
                stack.append(i)
            elif x==')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif x=='*':
                star.append(i)

        while stack and star:
            # if left parenthesi appeared after * 
            if stack[-1]>star[-1]:
                return False
            stack.pop()
            star.pop()
            
        return len(stack)==0
            