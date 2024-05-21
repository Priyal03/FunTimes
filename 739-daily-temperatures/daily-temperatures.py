class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for day, temp in enumerate((temperatures)):
            
            while stack and temp > temperatures[stack[-1]]:
                previousday=stack.pop()
                ans[previousday] = day - previousday

            stack.append(day)
        return ans
