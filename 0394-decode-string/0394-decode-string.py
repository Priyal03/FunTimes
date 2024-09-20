class Solution:
#     When we hit an opening bracket [, we push the current_str and current_num to the stack and reset them to start processing the new substring.
# When we hit a closing bracket ], we pop the stack to retrieve the previous string and the number k, then repeat the current string k times and append it to the previous string.
    def decodeString(self, s: str) -> str:
        stack=[]
        digit=0
        result=""

        for char in s:
            if char.isdigit():
                digit = digit*10 + int(char)
            elif char.isalpha():
                result+=char
            
            elif char=='[':
                stack.append((result,digit))
                result=""
                digit=0
            elif char==']':
                prev_str, num = stack.pop()
                result = prev_str+result*num
            
        return result