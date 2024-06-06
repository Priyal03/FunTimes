class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""
        phonemap = {'2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
        ans=[]
        curr=""
        
        def backtrack(i, curr):

            if i==len(digits):
                ans.append(curr)
                return

            letters = phonemap[digits[i]]
            for l in letters:
                backtrack(i+1,curr+l)
            
        backtrack(0,"")
        return ans