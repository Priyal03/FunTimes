class Solution:

    def isValid(self, s: str) -> bool:

        stack = []

        mapping={"(":")","{":"}","[":"]"}

        for chars in s:
            
            if chars in mapping:
                stack.append(chars)
            
            else:
                if not stack: #if stack is empty , then we do not have opening braces
                    return False

                popped = stack.pop()

                if mapping[popped] !=  chars: #if we can not find opening brace's pair in mapping to current element

                    return False
                
        return not stack # if stack is empty then string is valid