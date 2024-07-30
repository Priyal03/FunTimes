class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        #set answer only after finding the correct higher temperature, you can't fill up answer while traversing, thats why you must use stack to just add the temps as they come in line and calculate difference only when you find higher temperature.
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                popped = stack.pop()
                ans[popped]=i-popped
            stack.append(i)
        return ans