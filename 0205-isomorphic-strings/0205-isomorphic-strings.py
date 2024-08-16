class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def transform(input:str)->str:
            indexmap={}
            ans=[]
            for i,c in enumerate(input):
                if c not in indexmap:
                    indexmap[c]=i
                ans.append(indexmap[c])
            return ''.join(str(ans))
        
        return transform(s)==transform(t)