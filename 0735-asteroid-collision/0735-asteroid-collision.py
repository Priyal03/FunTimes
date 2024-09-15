class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        ans=[]
# We don't really need to add negative asteroids into stack.
# Consider stack as a barrier of positive asteroids that negative should pass
        for asteroid in asteroids:
            
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and abs(asteroid) > stack[-1] :
                    stack.pop() #if negative is higher we keep removing positives from stack

                if len(stack)==0: 
                    ans.append(asteroid)#if negative beats all positives

                elif stack[-1]==abs(asteroid):
                        stack.pop()

        ans+=stack
        return ans