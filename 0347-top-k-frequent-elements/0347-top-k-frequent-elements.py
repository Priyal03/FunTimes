from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occurrences = Counter(nums)#take count of each digit.
        
        bucket=[[] for _ in range (len(nums)+1)] #bucket create
        for digit, count in occurrences.items():
            bucket[count].append(digit)

        res=[]
        #traverse from highest and until k 
        for i in range(len(bucket)-1,-1,-1):
            while len(bucket[i])>0 and k>0:
                
                res.append(bucket[i].pop())
                k-=1
            
        return res