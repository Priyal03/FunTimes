class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s

        n=len(s)
        ans=[]
        sectionLength = (numRows-1)*2

        for currRow in range(numRows):
            index=currRow
            while index<n:
                ans.append(s[index]) # this is for all vertical characters after whole section.
                if currRow!=0 and currRow!=(numRows-1):
                    jump = sectionLength-2*currRow #(jump is only for the diagonal patterned characters)
                    middleIndex = index+jump
                    if middleIndex<n:
                        ans.append(s[middleIndex])

                index+=sectionLength
                
        return ''.join(ans)