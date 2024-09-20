from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = Counter(nums)#take count of each digit.
        
        result = sorted(hmap, key=hmap.get, reverse=True)

        return result[:k]