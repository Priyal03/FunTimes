class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        def allUnique(start,end):
            charSet = set()
            for i in range(start,end+1):   
                if s[i] in charSet:
                    return False
                charSet.add(s[i])
            return True
        
        maxLength=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if allUnique(i,j):
                    maxLength = max(maxLength, j-i+1)
        
        return maxLength

#time complexity O(n3) & space is size of substringSet --> O(min(size of string, size of charSet))
