class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s)%2==1:
            return False
            
        for c in s:
            if c=='{' or c=='(' or c=='[':
                stack.append(c)

            elif len(stack)==0:
                return False

            else:
                popped = stack.pop()

                if popped=='[' and c!=']':
                    return False
                if popped=='(' and c!=')':
                    return False
                if popped=='{' and c!='}':
                    return False
        
        return len(stack)==0