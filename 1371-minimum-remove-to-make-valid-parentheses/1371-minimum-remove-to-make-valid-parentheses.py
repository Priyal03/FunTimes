class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        removalSet=set()

        for i, curr in enumerate(s):
            if curr.isalpha():
                continue
            elif curr=='(':
                stack.append(i)
            elif not stack:
                removalSet.add(i)
            else:
                stack.pop()

        while stack:
            removalSet.add(stack.pop())

        result=[]
        for i,curr in enumerate(s):
            if i not in removalSet:
                result.append(curr)
# The overall time complexity remains O(n + m), where n is the length of s and m is the number of elements in indexesToDelete. However, using a list and joining it at the end avoids the quadratic time complexity associated with string concatenation in a loop. #
        return "".join(result)