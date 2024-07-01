class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count=[0]*len(edges)*2
        for x,y in edges:
            count[x]+=1
            count[y]+=1

        return count.index(max(count))