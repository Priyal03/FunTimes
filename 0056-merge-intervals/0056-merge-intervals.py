class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort = sorted(intervals, key=lambda x:x[0])
        ans=[sort[0]]
        
        for i in range(1,len(sort)):
            #current element's start must be smaller than last element's end
            if ans[-1][1]>=sort[i][0]: 
                #last element's end must be smaller than current's
                if ans[-1][1]<sort[i][1]: 
                    ans[-1][1]=sort[i][1]
                #else skip it as that interval is redundant
            else:
                ans.append(sort[i])   

        return ans