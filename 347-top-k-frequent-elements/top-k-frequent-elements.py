class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}

        for x in nums : 
            map[x]=map.get(x,0)+1

        sortedmap = sorted(map.items(), key=lambda items : items[1], reverse=True)
        res = []

        for i in range(len(sortedmap)):
        
            if k>0:
                res.append(sortedmap[i][0])
                k-=1

        return res

        