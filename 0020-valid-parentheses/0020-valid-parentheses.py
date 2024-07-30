class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                popped = stack.pop()
                if (
                    (popped == "[" and c != "]")
                    or (popped == "{" and c != "}")
                    or (popped == "(" and c != ")")
                ):
                    return False
        return len(stack) == 0
