class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            curr=[1]
            for j in range(1,i+1):#we need the last index as well in the final matrix limits so +1
                if j==i:
                    curr.append(1)
                else:
                    curr.append(ans[i-1][j-1]+ans[i-1][j])
            ans.append(curr)
        return ans