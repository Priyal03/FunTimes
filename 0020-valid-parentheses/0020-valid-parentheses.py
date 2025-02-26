class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        for curr in s:
            
            if curr=='[' or curr=='{' or curr=='(':
                stack.append(curr)

            else:
                if not stack:
                    return False

                top_element = stack.pop()
                if top_element == '[' and curr != ']':
                    return False
                elif top_element == '(' and curr != ')':
                    return False
                elif top_element == '{' and curr != '}':
                    return False

        return not stack