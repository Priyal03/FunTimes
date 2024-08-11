class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxelement = -1
        
        for i in range(len(arr)-1,-1,-1):
            
            temp = arr[i]
            arr[i]=maxelement
            maxelement = max(maxelement, temp)
        
        return arr