from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Occurrences = Counter(nums)
        #{1:3,2:2,3:1}
        #sort based on hash values in the decending order
        sortedValues = sorted(Occurrences.items(), key=lambda x:x[1], reverse=True)
        #remove the top k-1 elements from the sorted hashmap.values()
        res=[]
        
        for item in (sortedValues[:k]):
            
            res.append(item[0])
            
        return res