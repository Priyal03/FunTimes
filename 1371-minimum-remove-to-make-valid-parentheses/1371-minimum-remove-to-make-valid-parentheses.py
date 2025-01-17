class Solution:
    #two step process 
    # add extra ) when occurs and add extra ( after iterating.
    # use set to keep O(1) complexity and prepare the resultant string.
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indexToDelete = set()
        ans = []

        for i in range(len(s)):
            if s[i].isalpha():
                continue
            elif s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    indexToDelete.add(i)

        while stack:
            indexToDelete.add(stack.pop())

        for i in range(len(s)):
            if i not in indexToDelete:
                ans.append(s[i])

        return "".join(ans)
