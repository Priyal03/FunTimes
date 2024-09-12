class Solution:
    def reverseWords(self, s: str) -> str:
        def trim_spaces(s):
            n=len(s)
            left=0
            right=n-1
            while left<=right and s[left]==' ':
                left+=1
            while left<=right and s[right]==' ':
                right-=1
            ans=[]
            while left<=right:
                if s[left]!=' ':
                    ans.append(s[left])
                elif ans and ans[-1]!=' ':
                    ans.append(' ')
                left+=1
            return ans

        def reverse_list(inputStr,left,right):
            while left<right:
                inputStr[left],inputStr[right]=inputStr[right],inputStr[left]
                left+=1
                right-=1

        def reverse_each_word(word):
            n=len(word)
            start=0
            while start<n:
                end=start
                while end<n and word[end]!=' ':
                    end+=1
                reverse_list(word,start,end-1)
                start=end+1

        trimmed=trim_spaces(s)
        reverse_list(trimmed,0,len(trimmed)-1)
        reverse_each_word(trimmed)
        return ''.join(trimmed)