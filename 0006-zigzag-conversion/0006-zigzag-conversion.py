class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = []
        n = len(s)
        offset = (numRows-1)*2
        
        for i in range(numRows):
            index = i
            while index < n:
                ans.append(s[index])

                if i != 0 and i != (numRows - 1):
                    distanceBetween = offset - 2 * i
                    insideIndex = index + distanceBetween

                    if insideIndex < n:
                        ans.append(s[insideIndex])

                index += offset

        return "".join(ans)