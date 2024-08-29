class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for curr in asteroids:
            isBig = True
            while stack and stack[-1]>0 and curr < 0:
                if stack[-1]<abs(curr):
                    stack.pop()
                elif stack[-1]==abs(curr):
                    stack.pop()
                    isBig=False
                    break
                else:
                    isBig=False
                    break
            if isBig:
                stack.append(curr)
        return stack
                